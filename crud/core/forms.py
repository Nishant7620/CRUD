from django import forms
from .models import Model

class HomeForm(forms.ModelForm):
    class Meta:
        model = Model
        
        fields = ['name','heroic_name']