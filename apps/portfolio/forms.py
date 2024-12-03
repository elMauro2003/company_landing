from django import forms
from .models import *


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project_name', 'filter', 'description', 'image', 'button1_text', 'button2_text', 'button2_link']


class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['filter','filter_name']