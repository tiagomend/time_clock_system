from django.db import models

# Armazena dados dos Colaborades
class RegistrationCollab(models.Model):
    pis = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=30)
    status = models.BooleanField()
    admission = models.DateField()
    time_bank = models.BooleanField()
 
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=20)

class EventOccurrence(models.Model):
    event_collab_id = models.AutoField(primary_key=True)
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()

class TimeRegister(models.Model):
    key = models.CharField(primary_key=True, max_length=15)
    date = models.DateField()
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    entry_one = models.TimeField()
    entry_two = models.TimeField()
    entry_three = models.TimeField()
    exit_one = models.TimeField()
    exit_two = models.TimeField()
    exit_three = models.TimeField()
    month = models.IntegerField()

# Armazena Banco de Horas
class TimeBank(models.Model):
    time_bank_id = models.AutoField(primary_key=True)
    pis = models.ForeignKey(RegistrationCollab, on_delete=models.CASCADE)
    month = models.IntegerField()
    year = models.IntegerField()
    positive_hours = models.TimeField()
    negative_hours = models.TimeField()
    hours = models.TimeField()
