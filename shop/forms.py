from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="Entry the title")
