from django import forms
from .constant import BANK_CHOICE, STATUS_CHOICE
from django.forms.widgets import DateInput

class RegistrationCollabForm(forms.Form):
    name = forms.CharField(label='Nome' ,max_length=50)
    pis = forms.IntegerField(label='PIS')
    occupation = forms.CharField(label='Função' ,max_length=30)
    status = forms.ChoiceField(label='Situação', choices=STATUS_CHOICE)
    admission = forms.DateField(label='Admissão', widget=DateInput(attrs={'type':'date'}))
    time_bank = forms.ChoiceField(label='Modalidade', choices=BANK_CHOICE)

class EditCollabForm(forms.Form):
    status = forms.ChoiceField(label='Situação', choices=STATUS_CHOICE)
    time_bank = forms.ChoiceField(label='Modalidade' ,choices=BANK_CHOICE)
