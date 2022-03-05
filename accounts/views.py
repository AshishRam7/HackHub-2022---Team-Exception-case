from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                print("username present")
                # return render(request, 'sign up.html')
                return render(request, 'sign in.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                print("email present")
                # return render(request, 'sign up.html')
                return render(request, 'sign in.html')

            else:

                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user_created')
                messages.info(request, 'user created')
                return render(request, 'sign in.html')

        else:
            messages.info("password not matching")
            print("fgdgdfg")
            return redirect('/')
    else:
        messages.info(request, 'password not matching')
        print("fgdgdfgsafsfsfs")
        return render(request, 'sign up.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(user_name=username, password=password)

        if user is not None:
            login(request, user)
            print("Loggedin")
            return redirect('agri.html')

        else:
            print("Invalid duh")
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    else:
        print("Invalid duh2")
        return render(request, 'sign in.html')


def logout(request):
    authenticate.logout(request)
    return redirect('/')
