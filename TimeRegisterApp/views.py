from django.shortcuts import render
from django.http import HttpResponse
from .calculation import calculation
from .forms import RegistrationCollabForm
from .models import RegistrationCollab, TimeRegister
from . import crud
from .constant import INFO

# Função views da página de cadastro de colaboradores
def Collaborator(request):
    DataCollab = RegistrationCollab.objects.all()
    context =  {
        'DataCollab':DataCollab, 
        }
    if request.method == 'GET':
        return render(request, 'colaborador.html', context)
    if request.method == 'POST':
        if request.POST['form_name'] == "collab_form":
            UpdateError = crud.CreateCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador já existe')
        if request.POST['form_name'] == "form_delete_colab":
            UpdateError = crud.DeleteCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador não existe!')
        if request.POST['form_name'] == "edit_colab":
            UpdateError = crud.UpdateCollab(post=request.POST)
            if UpdateError == False:
                return render(request, 'colaborador.html', context)
            else:
                return HttpResponse('Colaborador não existe!')


# Função views da página de apontamento
def TimeNote(request):
    DataCollab = RegistrationCollab.objects.all()
    context =  {
        'DataCollab':DataCollab, 
        }
    if request.method == 'GET':
        return render(request, 'apontamento.html', context)
    if request.method == 'POST':
        if request.POST['form_name'] == 'manual':
            UpdateError = crud.CreateTimeRegister(post=request.POST)
            if UpdateError == True:
                Collab = RegistrationCollab.objects.get(
                    pis=int(request.POST['pis'])
                    )
                context.update({
                    'collab':str(Collab).upper()
                })
                return render(request, 'note_error_return.html', context)
            
            else:
                Collab = RegistrationCollab.objects.get(
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
                    'collab':str(Collab).upper()
                    })
                return render(request, 'note_success_return.html', context)


def TimeReport(request):
    DataCollab = RegistrationCollab.objects.all()
    context =  {
        'DataCollab':DataCollab, 
        }
    if request.method == 'GET':
        return render(request, 'relatorio.html', context)
    if request.method == 'POST':
        time_filter = crud.ReadTimeRegister(request.POST)
        collab = RegistrationCollab.objects.get(pis=request.POST['pis'])
        sum = calculation(time_filter)
        date = request.POST['date']
        context.update({
                'time_filter':sum['sum_list'],
                'sum_final':sum['sum_final'],
                'collab':collab,
                'date':date
                })
        if request.POST['form_name'] == 'filtro':
            return render(request, 'relatorio_return.html', context)
        if request.POST['form_name'] == 'edit_time':
            UpdateError = crud.UpdateTimeRegister(request.POST)
            if UpdateError == True:
                return HttpResponse('Apontamento inexistente!')
            else:
                return render(request, 'relatorio_return.html', context)
        elif request.POST['form_name'] == 'form_delete_time':
            UpdateError = crud.DeleteTimeRegister(request.POST)
            if UpdateError == True:
                return HttpResponse('Apontamento inexistente!')
            else:
                return render(request, 'relatorio_return.html', context)

