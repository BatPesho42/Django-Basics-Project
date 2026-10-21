from django.db import transaction
from django.db.models import Avg
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from common.forms import CommentForm

from recipes.forms import RecipeForm, RecipeIngredientFormSet, RecipeDeleteForm
from recipes.models import Recipe


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'
    context_object_name = 'recipes'
    ordering = [ 'category' ,'-created_at']
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset().annotate(average_rating=Avg('comments__rating'))

        min_rating = self.request.GET.get('min_rating')
        if min_rating and min_rating.isdigit():
            min_rating = int(min_rating)

            if 1 <= min_rating <= 5:
                qs = qs.filter(average_rating__gte=min_rating)

        recipe_category = self.request.GET.get('category')
        if recipe_category:
            qs = qs.filter(category=recipe_category)

        recipe_style = self.request.GET.get('style')
        if recipe_style:
            qs = qs.filter(style=recipe_style)

        return qs

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details.html'
    context_object_name = 'recipe'

    def get_queryset(self):
        return Recipe.objects.filter(pk=self.kwargs['pk']).prefetch_related('comments')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'comment_form' not in context:
            context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = self.object
            comment.save()
            return redirect('recipes:recipe-details', pk=self.object.pk)

        context = self.get_context_data(comment_form=form)
        return self.render_to_response(context)

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe-create.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'formset' not in context:
            if self.request.method == 'POST':
                formset = RecipeIngredientFormSet(self.request.POST)
            else:
                formset = RecipeIngredientFormSet()
            context.update({'formset': formset})

        return context

    def form_valid(self, form):
        formset = RecipeIngredientFormSet(self.request.POST)

        if not formset.is_valid():
            context = self.get_context_data(formset=formset, form=form)
            return self.render_to_response(context)

        with transaction.atomic():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('recipes:recipe-details', kwargs={'pk': self.object.pk})

class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe-edit.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'formset' not in context:
            recipe = self.object
            if self.request.method == 'POST':
                formset = RecipeIngredientFormSet(self.request.POST, instance=recipe)

            else:
                formset = RecipeIngredientFormSet(instance=recipe)

            context.update({'formset': formset})

        return context

    def form_valid(self, form):
        formset = RecipeIngredientFormSet(self.request.POST, instance=self.object)
        if not formset.is_valid():
            context = self.get_context_data(formset=formset, form=form)
            return self.render_to_response(context)

        with transaction.atomic():
            self.object = form.save()
            formset.save()

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('recipes:recipe-details', kwargs={'pk': self.object.pk})

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipes:recipe-list')
    form_class = RecipeDeleteForm
    template_name = 'recipes/recipe-delete.html'
    context_object_name = 'recipe'