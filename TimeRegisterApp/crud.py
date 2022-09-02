from calendar import month
from .models import RegistrationCollab, TimeRegister

# Funções CRUD do RegistrationCollab
def CreateCollab(post):
    requisition_data = post
    if RegistrationCollab.objects.filter(pis=requisition_data['pis']):
        return True
    else:
        Collab = RegistrationCollab.objects.create(
            pis=requisition_data['pis'],
            name=str(requisition_data['name']).title(),
            occupation=str(requisition_data['occupation']).title(),
            status=requisition_data['status'],
            admission=requisition_data['admission'],
            time_bank=requisition_data['time_bank']
        )
        Collab.save()
        return False

def UpdateCollab(post):
    requisition_data = post
    if RegistrationCollab.objects.filter(pis=requisition_data['pis']):
        RegistrationCollab.objects.filter(pis=requisition_data['pis']).update(
            occupation=requisition_data['occupation'],
            status=requisition_data['status'],
            time_bank=requisition_data['time_bank']
        )
        return False
    else:
        return True

def DeleteCollab(post):
    requisition_data = post
    if RegistrationCollab.objects.filter(pis=requisition_data['pis']):
        RegistrationCollab.objects.filter(pis=requisition_data['pis']).delete()
        return False
    else:
        return True

# Criação da chave-primária do TimeRegister
def KeyTimeRegister(date, pis):
    # date no formato '2022-09-08'
    create_key = str(
        date[8:10] + '/' +
        date[5:7] + '/' +
        date[0:4] + '-' +
        pis
        ) 
    return create_key


# Funções CRUD do TimeRegister
def CreateTimeRegister(post):
    requisition_data = post
    create_key = KeyTimeRegister(
        date=requisition_data['date'],
        pis=requisition_data['pis']
        )
    if TimeRegister.objects.filter(key=create_key):
        return True
    else:
        time = TimeRegister.objects.create(
            key=create_key,
            date=requisition_data['date'],
            pis=requisition_data['pis'],
            entry_one=requisition_data['entry_one'],
            entry_two=requisition_data['entry_two'],
            entry_three=requisition_data['entry_three'],
            exit_one=requisition_data['exit_one'],
            exit_two=requisition_data['exit_two'],
            exit_three=requisition_data['exit_three'],
            month=int(create_key[3:5]),
            info=requisition_data['info']
        )
        time.save()
        return False

def ReadTimeRegister(post):
    requisition_data = post

def UpdateTimeRegister(post):
    requisition_data = post

def DeleteTimeRegister(post):
    requisition_data = post