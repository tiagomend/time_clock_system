from .models import RegistrationCollab, TimeRegister

# Funções CRUD do RegistrationCollab
def CreateCollab(post):
    requisition_data = post
    if RegistrationCollab.objects.filter(pis=requisition_data['pis']):
        return True
    else:
        Collab = RegistrationCollab.objects.create(
            pis=requisition_data['pis'],
            name=str(requisition_data['name']).upper(),
            occupation=str(requisition_data['occupation']).upper(),
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

# Funções CRUD do TimeRegister
def CreateTimeRegister(post):
    return True

def ReadTimeRegister(post):
    requisition_data = post

def UpdateTimeRegister(post):
    requisition_data = post

def DeleteTimeRegister(post):
    requisition_data = post