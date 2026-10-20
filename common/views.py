from django import forms
from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView

from catalog.models import Ingredient
from common.forms import SearchBarForm, CommentDeleteForm
from common.models import RecipeComment
from recipes.models import Recipe


# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recent_recipes = Recipe.objects.order_by('-created_at')[:3]
        context['recent_recipes'] = recent_recipes
        return context


class SearchResultView(TemplateView):
    template_name = 'common/search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = SearchBarForm(self.request.GET)

        if form.is_valid() and form.cleaned_data['query'].strip():
            search = form.cleaned_data['query']
            recipes = Recipe.objects.filter(title__icontains=search)
            context.update({'recipes': recipes, 'search': search})


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

class CommentEditView(UpdateView):
    model = RecipeComment
    template_name = 'common/comment-edit.html'
    context_object_name = 'comment'

class CommentDeleteView(CommentDeleteForm):
    model = RecipeComment
    template_name = 'common/comment-delete.html'
    context_object_name = 'comment'