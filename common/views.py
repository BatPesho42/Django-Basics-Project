from django.shortcuts import render
from django.views.generic import TemplateView

from recipes.models import Recipe


# Create your views here.
class HomePageView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recent_recipes = Recipe.objects.order_by('-created_at')[:3]
        context['recent_recipes'] = recent_recipes
        return context