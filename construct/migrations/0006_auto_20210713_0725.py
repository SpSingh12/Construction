# Generated by Django 3.2.4 on 2021-07-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0005_auto_20210713_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Empid',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Sr. No'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Empname',
            field=models.CharField(max_length=100, verbose_name='Full Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Location',
            field=models.CharField(choices=[('Pune', 'rachi'), ('Bangalore', 'Banglore'), ('Jaipur', 'Jaipur'), ('Bagru', 'Bagru'), ('Ranchi', 'ranchi'), ('Mumbai', 'Mumbai'), ('Dehradun', 'Dehradun'), ('Bhilwara', 'Bhilwara'), ('Ajmer', 'Ajmer'), ('Bareilly', 'Bareilly'), ('Gujrat', 'Gujrat'), ('Alwar', 'Alwar'), ('Agra', 'Agra'), ('Kanpur', 'Kanpur'), ('jodhpur', 'Jodhpur'), ('Bikaner', 'Bikaner'), ('Vishakapatnam', 'Vishakapatnam'), ('Ahmedabad', 'Ahmedabad'), ('Delhi', 'Delhi'), ('Chandigarh', 'Chandigarh'), ('Dosa', 'Dosa')], default='Delhi', max_length=50, verbose_name='CITY'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Mobile',
            field=models.IntegerField(verbose_name='Contact No.'),
        ),
    ]
