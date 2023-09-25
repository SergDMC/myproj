from django import forms

from .models import Tel

class SearchForm(forms.Form): 
    query = forms.CharField()