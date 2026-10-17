from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from catalog.forms import IngredientForm
from catalog.models import Ingredient


# Create your views here.
class IngredientCreateView(CreateView):
    model = Ingredient
    success_url = reverse_lazy('home')
    form_class = IngredientForm
    template_name = 'catalog/ingredient-create.html'

class IngredientEditView(UpdateView):
    model = Ingredient
    success_url = reverse_lazy('home')
    form_class = IngredientForm
    template_name = 'catalog/ingredient-edit.html'

class IngredientDeleteView(DeleteView):
    model = Ingredient
    success_url = reverse_lazy('home')
    template_name = 'catalog/ingredient-delete.html'

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'catalog/ingredient-list.html'
    context_object_name = 'ingredients'