from django.forms import ModelForm
from django import forms

from catalog.models import Ingredient


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['created_at', 'updated_at']
        labels = {'name': 'Ingredient Name',
                  'description': 'Ingredient Description'}
        widgets = {"name": forms.TextInput(attrs={'placeholder': 'Ingredient Name'}),
                   "description": forms.Textarea(attrs={'placeholder': 'Tell us about this ingredient...'})}