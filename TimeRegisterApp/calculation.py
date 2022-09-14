from datetime import time, timedelta
from .constant import WEEKDAY

# Função para converter time em timedelta
def converter_timedelta(time):
    hrs, min, sec = map(int, str(time).split(':'))
    duration = timedelta(hours=hrs, minutes=min, seconds=sec)
    return duration


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
        sum_list.append(data_list)
    dict_return = {
        'sum_list':sum_list,
        'sum_final':[
            sum_regular, 
            sum_fifty_percent, 
            sum_hundred_percent
        ]
    }
    return dict_return
