from django.db.models import Avg
from django.shortcuts import render
from django.views.generic import ListView

from recipes.models import Recipe


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipe-list.html'
    context_object_name = 'recipes'
    ordering = [ 'category' ,'-created_at']

    def get_queryset(self):
        qs = super().get_queryset().annotate(average_rating=Avg('recipecomment__rating'))

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
