from django.db import models
from django import forms
from django.urls import reverse


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class DeleteFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['readonly'] = True

class CommentViewMixin:
    def get_queryset(self):
        qs = super().get_queryset().filter(recipe__pk=self.kwargs['pk'])
        return qs

    def get_success_url(self):
        return reverse('recipes:recipe-details', kwargs={'pk': self.object.recipe.pk})
