from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView, DeleteView, ListView

from catalog.models import Ingredient
from common.forms import SearchBarForm, CommentDeleteForm, CommentForm
from common.models import RecipeComment
from mixins import CommentViewMixin
from recipes.models import Recipe


# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recent_recipes = Recipe.objects.order_by('-created_at')[:3]
        context['recent_recipes'] = recent_recipes
        return context


class SearchResultView(ListView):
    template_name = 'common/search.html'
    context_object_name = 'recipes'
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        form = SearchBarForm(self.request.GET)

        if form.is_valid() and form.cleaned_data['query'].strip():
            search = form.cleaned_data['query']
            return Recipe.objects.filter(title__icontains=search)

        return Recipe.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchBarForm(self.request.GET)
        context['form'] = form
        return context

class ProfileView(TemplateView):
    template_name = "common/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({'recipes_count': Recipe.objects.count(),
                        'ingredients_count': Ingredient.objects.count(),
                        'comments_count': RecipeComment.objects.count()
                        })

        return context

class CommentEditView(CommentViewMixin, UpdateView):
    model = RecipeComment
    template_name = 'common/comment-edit.html'
    form_class = CommentForm
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_pk'


class CommentDeleteView(CommentViewMixin, DeleteView):
    model = RecipeComment
    template_name = 'common/comment-delete.html'
    form_class = CommentDeleteForm
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_pk'
