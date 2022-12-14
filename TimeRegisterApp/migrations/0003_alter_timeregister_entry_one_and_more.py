# Generated by Django 4.1 on 2022-10-17 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeRegisterApp', '0002_timeregister_info_alter_timeregister_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeregister',
            name='entry_one',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='timeregister',
            name='entry_three',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='timeregister',
            name='entry_two',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='timeregister',
            name='exit_one',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='timeregister',
            name='exit_three',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='timeregister',
            name='exit_two',
            field=models.TimeField(default=datetime.time(0, 0), null=True),
        ),
    ]
