from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import Department
# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,"invalid input")
            return redirect('login')

    return render(request,"login.html")



def register(request):
   if request.method== 'POST':
      username=request.POST['username']
      passowrd = request.POST['password']
      password1 = request.POST['password1']
      if passowrd==password1:
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=passowrd)
            user.save();
            return redirect('login')
            print("user created")
      else:
         messages.info(request,"Password noy matched")
         return redirect('register')
      return redirect('/')
   return render(request,'register.html')


def form(request):
    return render(request,'form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def result(request):
    name = request.GET['username']
    date = request.GET['date']
    age = request.GET['age']
    gender = request.GET['gender']
    phone = request.GET['phone']
    address = request.GET['address']

    return render(request,"result.html",{'name':name,'date':date,'gender':gender,'age':age,'phone':phone})

