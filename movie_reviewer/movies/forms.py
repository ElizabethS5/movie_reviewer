from django import forms

class SearchForm(forms.Form):
    search_input = forms.CharField(label='Search for a movie', max_length=100)