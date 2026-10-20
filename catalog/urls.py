from django.urls import path, include

from catalog.views import IngredientCreateView, IngredientEditView, IngredientDeleteView, IngredientListView, \
    IngredientDetailView

app_name = 'catalog'

urlpatterns = [
    path('', IngredientListView.as_view(), name='ingredient-list'),
    path('create/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('<int:pk>', include([
        path('', IngredientDetailView.as_view(), name='ingredient-detail'),
        path('edit/', IngredientEditView.as_view(), name='ingredient-edit'),
        path('delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),
    ]))
]