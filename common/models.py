from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from mixins import TimestampMixin


# Create your models here.
class RecipeComment(TimestampMixin):
    recipe = models.ForeignKey("recipes.Recipe", on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=5)
    photo = models.ImageField(upload_to="comments/", blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
