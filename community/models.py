from decimal import Decimal

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class RecipeComment(models.Model):
    recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MaxValueValidator(Decimal('5.0')), MinValueValidator(Decimal('1.0'))])
    photo = models.ImageField(upload_to="comments/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)