from django.urls import path

from recipes.views import RecipeListView, RecipeCreateView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create')

]