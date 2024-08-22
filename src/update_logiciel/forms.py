from django import forms
from .models import MiseAJour

class MiseAJourForm(forms.ModelForm):
    class Meta:
        model = MiseAJour
        fields = ['date', 'version_Logiciel', 'type_logiciel', 'client', 'poste_concerne', 'addresse_MAC', 'agent']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'type':'date'
                }),
            'version_Logiciel': forms.TextInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'placeholder':'Ex : v2.1.0'
                }),
            'type_logiciel': forms.Select(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md'
                }),
            'client': forms.TextInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'placeholder':'Entrer le nom du client:'
                }),
            'poste_concerne': forms.TextInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'placeholder':'Entrer le poste concerné: '
                }),
            'addresse_MAC': forms.TextInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'placeholder':'Ex:00:A1:C3:D4:E5'
                }),
            'agent': forms.TextInput(attrs={
                'class': 'mt-1 p-2 block w-full border-gray-300 rounded-md',
                'placeholder':'Entrer le nom de l\'agent:'
                })
        }
    


