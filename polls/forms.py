from django import forms
from .models import maclloc

class MacllocForm(forms.ModelForm):
    class Meta:
        model = maclloc
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact1','placeholder':'Name*'}),
            'mobile': forms.TextInput(attrs={'class': 'contact1','placeholder':'Mobile*'}),
            'email': forms.TextInput(attrs={'class': 'contact1','placeholder':'Email*'}),
            'message': forms.TextInput(attrs={'class': 'contact2','placeholder':'Message*'}),
        }
        fields = '__all__'


