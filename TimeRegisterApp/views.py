from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationCollabForm, EditCollabForm
from .models import RegistrationCollab
from .crud import CreateCollab, UpdateCollab, DeleteCollab

# Create your views here.
def Collaborator(request):
    DataCollab = RegistrationCollab.objects.all()
    context =  {
        'DataCollab':DataCollab, 
        }
    if request.method == 'GET':
        return render(request, 'colaborador.html', context)
    if request.method == 'POST':
        if request.POST['form_name'] == "collab_form":
            UpdateError = CreateCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador já existe')
        if request.POST['form_name'] == "form_delete_colab":
            UpdateError = DeleteCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador não existe!')
        if request.POST['form_name'] == "edit_colab":
            UpdateError = UpdateCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador não existe!')

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
