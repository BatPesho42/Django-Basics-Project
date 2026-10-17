from django.db import models

from mixins import TimestampMixin


# Create your models here.
class IngredientCategory(models.Model):
    class CategoryChoices(models.TextChoices):
        BASE = "Base", "Base ingredient"
        FLAVOURING = "Flavouring", "Flavouring"
        FERMENTABLE = "Fermentable", "Fermentable"
        FERMENTATION_AGENT = "Fermentation Agent", "Fermentation agent"
        ADDITIVE = "Additive", "Additive"
        CLARIFYING_AGENT = "Clarifying Agent", "Clarifying agent"

    name = models.CharField(max_length=50, unique=True, choices=CategoryChoices.choices)

    def __str__(self):
        return self.name

class Ingredient(TimestampMixin):
    name = models.CharField(max_length=50)
    categories = models.ManyToManyField(IngredientCategory, related_name="ingredients")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

