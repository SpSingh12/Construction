# Generated by Django 3.2.4 on 2021-07-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0021_alter_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Bangalore', 'Banglore'), ('Agra', 'Agra'), ('Kanpur', 'Kanpur'), ('Bhilwara', 'Bhilwara'), ('Pune', 'rachi'), ('Ajmer', 'Ajmer'), ('Vishakapatnam', 'Vishakapatnam'), ('Bagru', 'Bagru'), ('Gujrat', 'Gujrat'), ('Alwar', 'Alwar'), ('jodhpur', 'Jodhpur'), ('Bikaner', 'Bikaner'), ('Chandigarh', 'Chandigarh'), ('Jaipur', 'Jaipur'), ('Dosa', 'Dosa'), ('Bareilly', 'Bareilly'), ('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'), ('Ahmedabad', 'Ahmedabad'), ('Dehradun', 'Dehradun'), ('Ranchi', 'ranchi')], default='Delhi', max_length=50, verbose_name='CITY'),
        ),
    ]