from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationCollabForm
from .models import RegistrationCollab
from .crud import CreateCollab, UpdateCollab, DeleteCollab, CreateTimeRegister
from .constant import INFO

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

def TimeNote(request):
    DataCollab = RegistrationCollab.objects.all()
    context =  {
        'DataCollab':DataCollab, 
        }
    if request.method == 'GET':
        return render(request, 'apontamento.html', context)
    if request.method == 'POST':
        UpdateError = CreateTimeRegister(post=request.POST)
        if UpdateError == True:
            return HttpResponse('Apontamento já existe!')
        
        else:
            Collab = RegistrationCollab.objects.filter(
                pis=int(request.POST['pis'])
                )
            context.update({
                'pis':request.POST['pis'],
                'date':request.POST['date'],
                'entry_one':request.POST['entry_one'],
                'exit_one':request.POST['exit_one'],
                'entry_two':request.POST['entry_two'],
                'exit_two':request.POST['exit_two'],
                'entry_three':request.POST['entry_three'],
                'exit_three':request.POST['exit_three'],
                'info':INFO[request.POST['info']],
                'collab':Collab
                })
            return render(request, 'return.html', context)
