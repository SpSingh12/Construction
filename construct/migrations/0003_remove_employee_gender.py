# Generated by Django 3.2.4 on 2021-07-12 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0002_auto_20210712_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
    ]
