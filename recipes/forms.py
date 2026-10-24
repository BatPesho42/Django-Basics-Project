from django.forms import ModelForm, inlineformset_factory
from django import forms

from mixins import DeleteFormMixin
from recipes.models import RecipeIngredient, Recipe



class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        exclude = ['recipe']
        labels = {
            'ingredient': 'Choose an ingredient',
            'quantity': 'Amount',
            'stage': 'When to add',
        }
        widgets = {
            'ingredient': forms.Select(),
            'role': forms.Select(),
            'quantity': forms.NumberInput(attrs={'placeholder': 'How much?'}),
            'unit': forms.Select(),
            'stage': forms.TextInput(attrs={'placeholder': 'e.g. Boil - 10 min'}),
            'notes': forms.TextInput(attrs={'placeholder': 'Optional notes...'}),
        }

RecipeIngredientFormSet = inlineformset_factory(Recipe, RecipeIngredient, form=RecipeIngredientForm, extra=12, can_delete=True)

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created_at', 'updated_at', 'ingredients']
        labels = {'aging_days': 'Aging',
                  'target_abv': 'Target ABV',
                  }
        widgets = {"title": forms.TextInput(attrs={'placeholder': 'Recipe Title'}),
                   'category': forms.Select(),
                   'style': forms.Select(),
                   "description": forms.Textarea(attrs={'placeholder': 'Add instructions...'}),
                   'photo': forms.FileInput(attrs={'placeholder': 'Upload a photo...'}),
                   'primary_fermentation_days': forms.NumberInput(attrs={'placeholder': 'e.g. 3 days in an open fermenter'}),
                   'secondary_fermentation_days': forms.NumberInput(attrs={'placeholder': 'optional; e.g. 7 days in a closed fermenter'}),
                   'aging_days': forms.NumberInput(attrs={'placeholder': 'optional; e.g. 10 days after bottling'}),
                   'target_abv': forms.NumberInput(attrs={'placeholder': 'e.g. 5.5%'}),
                   }

