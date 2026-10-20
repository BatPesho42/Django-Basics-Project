from django import forms

from common.models import RecipeComment
from mixins import DeleteFormMixin


class SearchBarForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Search recipes...'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = RecipeComment
        exclude = ['recipe', 'created_at', 'updated_at']
        widgets = {'comment': forms.Textarea(attrs={'placeholder': 'What do you think about this recipe?'})}

class CommentDeleteForm(CommentForm, DeleteFormMixin):
    ...