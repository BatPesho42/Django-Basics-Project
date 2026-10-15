from django.db import models

from mixins import TimestampMixin


# Create your models here.
class IngredientCategory(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Ingredient(TimestampMixin):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("IngredientCategory", on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

