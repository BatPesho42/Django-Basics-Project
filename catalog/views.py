from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from catalog.forms import IngredientForm
from catalog.models import Ingredient


# Create your views here.
class IngredientCreateView(CreateView):
    model = Ingredient
    success_url = reverse_lazy('catalog:ingredient-list')
    form_class = IngredientForm
    template_name = 'catalog/ingredient-create.html'
    context_object_name = 'ingredient'

class IngredientEditView(UpdateView):
    model = Ingredient
    success_url = reverse_lazy('catalog:ingredient-list')
    form_class = IngredientForm
    template_name = 'catalog/ingredient-edit.html'
    context_object_name = 'ingredient'


class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('catalog:ingredient-list')
    template_name = 'catalog/ingredient-delete.html'
    context_object_name = 'ingredient'


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'catalog/ingredient-list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'catalog/ingredient-details.html'
    context_object_name = 'ingredient'
