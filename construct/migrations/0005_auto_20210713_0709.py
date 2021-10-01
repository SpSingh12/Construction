# Generated by Django 3.2.4 on 2021-07-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0004_auto_20210712_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Dehradun', 'Dehradun'), ('Jaipur', 'Jaipur'), ('Delhi', 'Delhi'), ('Pune', 'rachi'), ('Ranchi', 'ranchi'), ('Mumbai', 'Mumbai'), ('Bangalore', 'Banglore')], default='Delhi', max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Password',
            field=models.CharField(help_text='YOUR PASSWORD', max_length=30, unique=True),
        ),
    ]