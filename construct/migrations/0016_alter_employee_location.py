# Generated by Django 3.2.4 on 2021-07-13 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0015_alter_employee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Bangalore', 'Banglore'), ('Bagru', 'Bagru'), ('Alwar', 'Alwar'), ('Kanpur', 'Kanpur'), ('Bareilly', 'Bareilly'), ('Pune', 'rachi'), ('Ahmedabad', 'Ahmedabad'), ('Dehradun', 'Dehradun'), ('Vishakapatnam', 'Vishakapatnam'), ('Gujrat', 'Gujrat'), ('Chandigarh', 'Chandigarh'), ('jodhpur', 'Jodhpur'), ('Dosa', 'Dosa'), ('Bikaner', 'Bikaner'), ('Ranchi', 'ranchi'), ('Delhi', 'Delhi'), ('Ajmer', 'Ajmer'), ('Jaipur', 'Jaipur'), ('Bhilwara', 'Bhilwara'), ('Agra', 'Agra')], default='Delhi', max_length=50, verbose_name='CITY'),
        ),
    ]
