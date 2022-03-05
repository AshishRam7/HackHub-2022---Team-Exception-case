from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        
        if password1==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return render(request,'sign up.html')
                
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return render(request,'sign up.html')
                
                
            
            else:
            
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user_created')
                messages.info(request,'user created')
                return render(request,'sign in.html')
               

        else:
            messages.info("password not matching")
            return redirect('/')
    else:
        messages.info(request,'password not matching')
        return render(request,'sign up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password1 = request.POST['password1']

        user = authenticate(user_name=username, password=password1)

        if user is not None:
            login(request, user)
            return redirect('agri.html')

        else:
            messages.info(request,'invalid credentials')
            return render(request,'agri.html')
    else:
        return render(request,'sign in.html')


def logout(request):
    authenticate.logout(request)
    return redirect('/')