from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from catalog.forms import IngredientForm
from catalog.models import Ingredient


# Create your views here.
class IngredientCreateView(CreateView):
    model = Ingredient
    success_url = reverse_lazy('home')
    form_class = IngredientForm