from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationCollabForm, EditCollabForm
from .models import RegistrationCollab
from .crud import CreateCollab, UpdateCollab, DeleteCollab

# Create your views here.
def Collaborator(request):
    FormCollab = RegistrationCollabForm()
    DataCollab = RegistrationCollab.objects.all()
    EditCollab = EditCollabForm()
    context =  {
        'FormCollab':FormCollab, 
        'DataCollab':DataCollab, 
        'EditCollab':EditCollab
        }
    if request.method == 'GET':
        return render(request, 'test.html', context)
    if request.method == 'POST':
        UpdateError = CreateCollab(post=request.POST)
        if UpdateError == False:
            return HttpResponse('Dados Salvos com sucesso!')
        else:
            return HttpResponse('Colaborador já existe')

def test(request):
    FormCollab = RegistrationCollabForm()
    if request.method == 'GET':
        return render(request, 'test.html', {'FormCollab':FormCollab})
    if request.method == 'POST':
        UpdateError = CreateCollab(post=request.POST)
        if UpdateError == False:
            return HttpResponse('Dados cadastrados com sucesso!')
        else:
            return HttpResponse('Dados existentes!')
