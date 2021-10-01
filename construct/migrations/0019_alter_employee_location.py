# Generated by Django 3.2.4 on 2021-07-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0018_alter_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Bhilwara', 'Bhilwara'), ('Jaipur', 'Jaipur'), ('Bangalore', 'Banglore'), ('Agra', 'Agra'), ('Bikaner', 'Bikaner'), ('Ahmedabad', 'Ahmedabad'), ('Dehradun', 'Dehradun'), ('Vishakapatnam', 'Vishakapatnam'), ('Chandigarh', 'Chandigarh'), ('Bareilly', 'Bareilly'), ('Ajmer', 'Ajmer'), ('Ranchi', 'ranchi'), ('Delhi', 'Delhi'), ('Dosa', 'Dosa'), ('Pune', 'rachi'), ('Kanpur', 'Kanpur'), ('Mumbai', 'Mumbai'), ('jodhpur', 'Jodhpur'), ('Alwar', 'Alwar'), ('Gujrat', 'Gujrat'), ('Bagru', 'Bagru')], default='Delhi', max_length=50, verbose_name='CITY'),
        ),
    ]
