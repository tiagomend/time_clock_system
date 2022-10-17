from datetime import timedelta
from .constant import WEEKDAY
from .models import RegistrationCollab, TimeBank
from .crud import update_time_bank

# Função para converter time em timedelta
def converter_timedelta(time):
    hrs, min, sec = map(int, str(time).split(':'))
    duration = timedelta(hours=hrs, minutes=min, seconds=sec)
    return duration

def extract_pis(key):
    # formato do key - '08/09/2022-12345678910'
    pis = key[11:]
    return pis

def calculation_time_bank(obj):
    pis = extract_pis(key=obj['sum_list'][0][0])
    collab = RegistrationCollab.objects.get(
        pis=pis
        )
    if collab.time_bank == True:
        print("True")
        update_time_bank(pis_p=pis, obj=obj)
    else:
        print('False')
    

def calculation(obj):
    timetables = obj
    sum_list = []
    default = timedelta(hours=8, minutes=55)
    sum_regular = timedelta(0)
    sum_fifty_percent = timedelta(0)
    sum_hundred_percent = timedelta(0)
    
    for data in timetables:
        entry_one = converter_timedelta(data.entry_one)
        exit_one = converter_timedelta(data.exit_one)
        entry_two = converter_timedelta(data.entry_two)
        exit_two = converter_timedelta(data.exit_two)
        entry_three = converter_timedelta(data.entry_three)
        exit_three = converter_timedelta(data.entry_three)
        sum = (exit_one - entry_one) + (exit_two - entry_two) + (exit_three - entry_three)
        
    
        if data.date.strftime("%A") == 'Saturday':
            regular = timedelta(0)
            fifty_percent = sum
            hundred_percent = timedelta(0)
        elif data.date.strftime("%A") == 'Sunday':
            regular = timedelta(0)
            fifty_percent = timedelta(0)
            hundred_percent = sum
        else:
            if sum >= default:
                regular = timedelta(hours=8, minutes=45)
                fifty_percent = sum - regular
                hundred_percent = timedelta(0)
            else:
                regular = sum
                fifty_percent = timedelta(0)
                hundred_percent = timedelta(0)
        data_list = [
            data.key,
            data.date, 
            WEEKDAY[data.date.strftime("%A")],
            data.entry_one,
            data.exit_one,
            data.entry_two,
            data.exit_two,
            data.entry_three,
            data.exit_three,
            regular, 
            fifty_percent, 
            hundred_percent
            ]
        sum_regular += regular
        sum_fifty_percent += fifty_percent
        sum_hundred_percent += hundred_percent
        sum_list.append(data_list) # A cada loop data_list será inserido no objeto sum_list

    # A variável dict_return é um dicionário que contém duas chaves.
    # A chave 'sum_list' contém os dados da soma das horas de cada dia.
    # A chave 'sum_final' contém objetos que armazenam a soma das horas normais, e extras (50% e 100%).
    dict_return = {
        'sum_list':sum_list,
        'sum_final':[
            sum_regular, 
            sum_fifty_percent, 
            sum_hundred_percent
        ]
    }
    calculation_time_bank(dict_return)
    return dict_return
