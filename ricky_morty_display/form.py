from django import forms


class DataForm(forms.Form):
    gender = forms.CharField(max_length=256)
    species = forms.CharField(max_length=256)
    
    