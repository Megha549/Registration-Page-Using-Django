from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

'''def members(request):
    return HttpResponse("Hello world!")'''
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']
        # Checking if the passwords match
        if password == confirm_password:
            if (User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
                messages.info(request,'Username already exist')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,email=email,first_name=first_name,password=password)
                user.set_password(password)
                user.save()
                print('success')
                return redirect('login_user')
    else:
       print('this is not post method')
       return render(request,"register.html")

def  login_user(request):
    if request.method== 'POST':
        username =request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login_user')
    else:    
         return render(request,"login.html")

def logout_user(request):
    auth.logout(request)
    return redirect('home')
