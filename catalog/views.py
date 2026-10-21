from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
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

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, 'Cannot delete ingredient that is used in a recipe.')
            return redirect('catalog:ingredient-details', pk=self.object.pk)


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'catalog/ingredient-list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'catalog/ingredient-details.html'
    context_object_name = 'ingredient'
