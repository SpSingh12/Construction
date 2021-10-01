# Generated by Django 3.2.4 on 2021-07-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0010_auto_20210713_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Gender',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Bagru', 'Bagru'), ('Gujrat', 'Gujrat'), ('Jaipur', 'Jaipur'), ('Chandigarh', 'Chandigarh'), ('Dosa', 'Dosa'), ('Delhi', 'Delhi'), ('Alwar', 'Alwar'), ('Bikaner', 'Bikaner'), ('Agra', 'Agra'), ('jodhpur', 'Jodhpur'), ('Pune', 'rachi'), ('Bhilwara', 'Bhilwara'), ('Kanpur', 'Kanpur'), ('Dehradun', 'Dehradun'), ('Ranchi', 'ranchi'), ('Ahmedabad', 'Ahmedabad'), ('Ajmer', 'Ajmer'), ('Bareilly', 'Bareilly'), ('Bangalore', 'Banglore'), ('Mumbai', 'Mumbai'), ('Vishakapatnam', 'Vishakapatnam')], default='Delhi', max_length=50, verbose_name='CITY'),
        ),
    ]
