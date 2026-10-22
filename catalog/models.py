from django.db import models

from mixins import TimestampMixin


class Ingredient(TimestampMixin):
    class CategoryChoices(models.TextChoices):
        BASE = "Base", "Base ingredient"
        FLAVOURING = "Flavouring", "Flavouring"
        FERMENTABLE = "Fermentable", "Fermentable"
        FERMENTATION_AGENT = "Fermentation Agent", "Fermentation agent"
        ADDITIVE = "Additive", "Additive"
        CLARIFYING_AGENT = "Clarifying Agent", "Clarifying agent"

    name = models.CharField(max_length=50)
    categories = models.CharField(max_length=20, choices=CategoryChoices.choices)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

