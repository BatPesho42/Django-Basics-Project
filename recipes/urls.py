from django.urls import path, include

from common.views import CommentEditView, CommentDeleteView
from recipes.views import RecipeListView, RecipeCreateView, RecipeDetailView, RecipeEditView, RecipeDeleteView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('<int:pk>/', include([
        path('', RecipeDetailView.as_view(), name='recipe-details'),
        path('edit/', RecipeEditView.as_view(), name='recipe-edit'),
        path('delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
        path('comment/<int:comment_pk>/', include([
            path('edit/', CommentEditView.as_view(), name='recipe-comment-edit'),
            path('delete/', CommentDeleteView.as_view(), name='recipe-comment-delete'),
        ])),

    ]))

]
