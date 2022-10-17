from django.db import models
from datetime import time

# Armazena dados dos Colaborades
class RegistrationCollab(models.Model):
    pis = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    status = models.BooleanField()
    admission = models.DateField()
    time_bank = models.BooleanField()

    def __str__(self):
        return self.name
 
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=20)

class EventOccurrence(models.Model):
    event_collab_id = models.AutoField(primary_key=True)
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()

class TimeRegister(models.Model):
    key = models.CharField(primary_key=True, max_length=30)
    date = models.DateField()
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    entry_one = models.TimeField(null=True, default=time(0, 0, 0))
    entry_two = models.TimeField(null=True, default=time(0, 0, 0))
    entry_three = models.TimeField(null=True, default=time(0, 0, 0))
    exit_one = models.TimeField(null=True, default=time(0, 0, 0))
    exit_two = models.TimeField(null=True, default=time(0, 0, 0))
    exit_three = models.TimeField(null=True, default=time(0, 0, 0))
    month = models.IntegerField()
    info = models.IntegerField(default=1)

# Armazena Banco de Horas
class TimeBank(models.Model):
    time_bank_id = models.AutoField(primary_key=True)
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    positive_hours = models.IntegerField()
    negative_hours = models.IntegerField()
    hours = models.IntegerField()
