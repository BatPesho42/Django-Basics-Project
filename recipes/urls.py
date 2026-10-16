from django.urls import path

from recipes.views import RecipeListView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),

]