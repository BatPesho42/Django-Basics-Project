from django.core.exceptions import ValidationError
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
    categories = models.JSONField(default=list)
    description = models.TextField(blank=True, null=True)

    @property
    def category_labels(self):
        choices = dict(self.CategoryChoices.choices)
        labels = [choices.get(l, l) for l in self.categories]
        return labels

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.categories == []:
            raise ValidationError("At least one category must be selected")