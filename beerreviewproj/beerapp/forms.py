from django import forms
from .models import Beer, BeerType, Review

class BeerForm(forms.ModelForm):
    class Meta:
        model=Beer
        fields='__all__'