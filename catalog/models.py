from django.db import models

# Create your models here.
class IngredientCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey("IngredientCategory", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

