from django import forms
from .models import Review


class SearchForm(forms.Form):
    query = forms.CharField(max_length=50, label='Search...')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # o modelo que queremos editar
        fields = ('title', 'score', 'review') # só os campos que o user vai inserir