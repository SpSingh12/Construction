from django import forms
from django.forms import fields, widgets
from django.forms.forms import Form
from .models import Employee




class Empform(forms.ModelForm):
    Password = forms.CharField(label='Password',widget=forms.PasswordInput,min_length=5,max_length=20)
    class Meta:
        model = Employee
        fields = ('Empid','Empname','Email','Mobile','Password','Location')

        # widget used form beautify the input fields of contact form
        widgets = {
            'Empname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'Password':forms.TextInput(attrs={'class':'form-control'}),
       
        }


# for login page

class Signinform(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput,min_length=5,max_length=20)
    class Meta:
        model = Employee
        fields = ['Email','Password']

    