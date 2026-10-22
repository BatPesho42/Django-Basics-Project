from django.core.exceptions import ValidationError
from django.db import models

from mixins import TimestampMixin
from validators import validate_positive


# Create your models here.
class Recipe(TimestampMixin):
    class CategoryChoices(models.TextChoices):
        BEER = "Beer", "Beer"
        WINE = "Wine", "Wine"
        OTHER = "Other", "Other"

    class StyleChoices(models.TextChoices):
        LAGER = "Lager", "Lager"
        ALE = "Ale", "Ale"
        SOUR = "Sour", "Sour"
        RED = "Red", "Red"
        WHITE = "White", "White"
        ROSE = "Rose", "Rose"
        SPARKLING = "Sparkling", "Sparkling"
        MEAD = "Mead", "Mead"
        CIDER = "Cider", "Cider"
        KOMBUCHA = "Kombucha", "Kombucha"
        GINGER_BEER = "Ginger Beer", "Ginger Beer"
        OTHER = "Other", "Other"

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CategoryChoices.choices)
    style = models.CharField(max_length=15, choices=StyleChoices.choices)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="recipes/", blank=True, null=True)
    primary_fermentation_days = models.PositiveIntegerField(default=0)
    secondary_fermentation_days = models.PositiveIntegerField(blank=True, null=True)
    aging_days = models.PositiveIntegerField(blank=True, null=True)
    target_abv = models.DecimalField(max_digits=3, decimal_places=1, validators=[validate_positive])
    ingredients = models.ManyToManyField('catalog.Ingredient', through='RecipeIngredient', related_name='recipes')


    def __str__(self):
        return self.title

    def clean(self):
        super().clean()

        if self.category == self.CategoryChoices.WINE and self.style not in [self.StyleChoices.RED, self.StyleChoices.WHITE, self.StyleChoices.ROSE, self.StyleChoices.SPARKLING, self.StyleChoices.OTHER]:
            raise ValidationError("Wine must be red, white, rose or sparkling")
        if self.category == self.CategoryChoices.BEER and self.style not in [self.StyleChoices.LAGER, self.StyleChoices.ALE, self.StyleChoices.SOUR, self.StyleChoices.OTHER]:
            raise ValidationError("Beer must be lager, ale or sour")
        if self.category == self.CategoryChoices.OTHER and self.style not in [self.StyleChoices.OTHER, self.StyleChoices.MEAD, self.StyleChoices.CIDER, self.StyleChoices.KOMBUCHA, self.StyleChoices.GINGER_BEER]:
            raise ValidationError("The Other category does not include wine or beer styles")

class RecipeIngredient(models.Model):
    class RoleChoices(models.TextChoices):
        MAIN = "Main", "Main"
        SECONDARY = "Secondary", "Secondary"
        AGENT = "Agent", "Agent"

    class UnitChoices(models.TextChoices):
        GRAMS = "g", "g"
        KILOGRAMS = "kg", "kg"
        LITERS = "l", "l"
        MILLILITERS = "ml", "ml"


    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey('catalog.Ingredient', on_delete=models.PROTECT)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, validators=[validate_positive])
    unit = models.CharField(max_length=5, choices=UnitChoices.choices)
    stage = models.CharField(max_length=30, blank=True, null=True)
    notes = models.CharField(max_length= 60, blank=True, null=True)
