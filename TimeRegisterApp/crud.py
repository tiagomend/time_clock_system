from .models import RegistrationCollab, TimeRegister, TimeBank
from datetime import timedelta

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
            pis=RegistrationCollab.objects.get(
                pis=requisition_data['pis']
            ),
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

def ReadTimeRegister(date, pis):
    # Formato da entrada 'pis': ['12345678910'], 'date': ['2022-09']
    data = TimeRegister.objects.filter(
        pis=pis,
        date__year=date[0:4],
        month=date[5:7]
        )
    return data

def UpdateTimeRegister(post):
    requisition_data = post
    if TimeRegister.objects.filter(key=requisition_data['key']):
        TimeRegister.objects.filter(key=requisition_data['key']).update(
            entry_one=requisition_data['entry_one'],
            exit_one=requisition_data['exit_one'],
            entry_two=requisition_data['entry_two'],
            exit_two=requisition_data['exit_two'],
            entry_three=requisition_data['entry_three'],
            exit_three=requisition_data['exit_three'],
        )
        return False
    else:
        return True

def DeleteTimeRegister(post):
    requisition_data = post
    if TimeRegister.objects.filter(key=requisition_data['key']):
        TimeRegister.objects.filter(key=requisition_data['key']).delete()
        return False
    else:
        return True

def update_time_bank(pis_p, obj):
    if TimeBank.objects.filter(
            pis=pis_p,
            month=int(obj['sum_list'][1][0][3:5]),
            year=int(obj['sum_list'][1][0][6:10]),
        ):
        time_bank = TimeBank.objects.get(
            pis=pis_p,
            month=int(obj['sum_list'][1][0][3:5]),
            year=int(obj['sum_list'][1][0][6:10]),
        )
        hours = obj['sum_final'][1].total_seconds() + obj['sum_final'][2].total_seconds()
        if time_bank.positive_hours == hours:
            pass
        else:
            time_bank.positive_hours = hours
            time_bank.negative_hours = hours - time_bank.negative_hours
            time_bank.save()

    else:
        time_bank = TimeBank.objects.create(
            pis=RegistrationCollab.objects.get(
                pis=pis_p
            ),
            month=int(obj['sum_list'][1][0][3:5]),
            year=int(obj['sum_list'][1][0][6:10]),
            positive_hours=obj['sum_final'][1].total_seconds() + obj['sum_final'][2].total_seconds(),
            negative_hours=0,
            hours=obj['sum_final'][1].total_seconds() + obj['sum_final'][2].total_seconds(),
            )
        time_bank.save()
        print(obj['sum_final'][1] + obj['sum_final'][2])
        print('Deu certo!')
        return True
