from .forms import Empform, Signinform
from django.shortcuts import redirect, render
# from django.http import HttpResponse
# Create your views here.
from.models import Employee


# details of forms
def show(request):
    data = Employee.objects.all()
    return render(request, 'construct/detail.html', {'mydata': data})


# html main sections
def home(request):
    return render(request, "construct/home.html")


def about(request):
    return render(request, 'construct/about.html')


def project(request):
    return render(request, 'construct/project.html')


def services(request):
    return render(request, 'construct/services.html')

# def contact(request):
#     return render(request,'construct/contact.html')

# use for contact form


def contact(request):
    if request.method == 'GET':
        form = Empform()
    if request.method == 'POST':
        form = Empform(request.POST)
        form.save()
        return redirect('show')
    # form = Empform()
    return render(request, 'construct/contact.html', {'myform': form})


# view action for login

def Signin(request):
    if request.method == 'POST':
        form = Signinform(request.POST)

        q = Employee.objects.filter(
            Email = request.POST['Email'],
            Password = request.POST['Password'])


        if len(q)>0:
            return redirect('show')

        else:
            return redirect('login')

    else:
        form = Signinform()
    return render(request,'construct/signin.html',{'formss' : form})




# VIEW ACTION FOR DELETE DATA
def Delete(request):
    email = request.GET['email']
    Employee.objects.filter(Email = email).delete()
    return redirect('show')


def residential(request):
    return render(request, 'construct/residential.html')

def residential_2(request):
    return render(request, 'construct/residential_2.html')

def residential_1(request):
    return render(request, 'construct/residential_1.html')

def hospital(request):
    return render(request, 'construct/hospital.html')

def commercial_2(request):
    return render(request, 'construct/commercial_2.html')

def all_project(request):
    return render(request, 'construct/all_project.html')