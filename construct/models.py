from django.db import models

# Create your models here.
class Employee(models.Model):
    LOCATION_CHOICE = {
        ('Delhi','Delhi'),
        ('Mumbai','Mumbai'),
        ('Jaipur','Jaipur'),
        ('Bangalore','Banglore'),
        ('Pune','rachi'),
        ('Ranchi','ranchi'),
        ('Dehradun','Dehradun'),
        ('Agra','Agra'),
        ('Ahmedabad','Ahmedabad'),
        ('Gujrat','Gujrat'),
        ('Chandigarh','Chandigarh'),
        ('Vishakapatnam','Vishakapatnam'),
        ('Ajmer','Ajmer'),
        ('Kanpur','Kanpur'),
        ('Alwar','Alwar'),
        ('Dosa','Dosa'),
        ('Bagru','Bagru'),
        ('Bareilly','Bareilly'),
        ('Bikaner','Bikaner'),
        ('jodhpur','Jodhpur'),
        ('Bhilwara','Bhilwara')
    }
    Location = models.CharField(verbose_name='CITY' ,max_length=50,choices=LOCATION_CHOICE,default='Delhi')
    Empid = models.AutoField(verbose_name='Sr. No' ,primary_key=True)
    Empname = models.CharField(verbose_name='Full Name',max_length=100)
    Email = models.EmailField(verbose_name='Email (Your Username)',max_length=100)
    Mobile = models.IntegerField(verbose_name='Contact No.')
    Password = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.Empname + " " + self.Email + " " + str(self.Mobile) + " " + self.Password  + " " + self.Location