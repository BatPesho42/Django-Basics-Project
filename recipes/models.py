from django.db import models

from catalog.models import Ingredient


# Create your models here.
class Recipe(models.Model):
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

    title = models.CharField(max_length=50)
    category = models.CharField(max_length=5, choices=CategoryChoices.choices)
    style = models.CharField(max_length=15, choices=StyleChoices.choices)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="recipes/", blank=True, null=True)
    primary_fermentation_days = models.IntegerField(),
    secondary_fermentation_days = models.IntegerField(blank=True, null=True),
    aging_days = models.IntegerField(blank=True, null=True),
    target_abv = models.DecimalField(max_digits=3, decimal_places=1),
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=5, choices=UnitChoices.choices)
    stage = models.CharField(max_length=30, blank=True, null=True)
    notes = models.CharField(max_length= 60, blank=True, null=True)
