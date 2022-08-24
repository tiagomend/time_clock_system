# Generated by Django 4.1 on 2022-08-17 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationCollab',
            fields=[
                ('pis', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('admission', models.DateField()),
                ('time_bank', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeRegister',
            fields=[
                ('key', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('entry_one', models.TimeField()),
                ('entry_two', models.TimeField()),
                ('entry_three', models.TimeField()),
                ('exit_one', models.TimeField()),
                ('exit_two', models.TimeField()),
                ('exit_three', models.TimeField()),
                ('month', models.IntegerField()),
                ('pis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeRegisterApp.registrationcollab')),
            ],
        ),
        migrations.CreateModel(
            name='TimeBank',
            fields=[
                ('time_bank_id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('positive_hours', models.TimeField()),
                ('negative_hours', models.TimeField()),
                ('hours', models.TimeField()),
                ('pis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeRegisterApp.registrationcollab')),
            ],
        ),
        migrations.CreateModel(
            name='EventOccurrence',
            fields=[
                ('event_collab_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeRegisterApp.event')),
                ('pis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TimeRegisterApp.registrationcollab')),
            ],
        ),
    ]