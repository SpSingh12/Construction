# Generated by Django 3.2.4 on 2021-07-12 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0003_remove_employee_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='RePassword',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='city',
        ),
    ]
