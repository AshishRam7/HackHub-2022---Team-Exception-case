from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import auth

# Create your views here.

def get_email():
    return email

def register(request):
    global email
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
            messages.info(request, "password not matching")
            print("fgdgdfg")
            return redirect('/')
    else:
        messages.info(request, 'password not matching')
        print("fgdgdfgsafsfsfs")
        return render(request, 'sign up.html')


def login(request):
    '''
    if request.method == 'POST':
        username = request.POST.get['user_name']
        password = request.POST.get['password']

        user = authenticate(user_name=username, password=password)

        if user is not None:
            login(request, user)
            print("Loggedin")
            return redirect('agri.html')

        else:
            print("Invalid duh")
            messages.info(request, 'invalid credentials')
            return render(request, 'agri.html')
    else:
        print("Invalid duh2")
        return render(request, 'sign.html')

'''


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('../')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'sign in.html')


def logout(request):
    auth.logout(request)
    return render(request, 'agri.html')


def admin_page(request):
    if not request.user.is_authenticated():
        return redirect('sign in.html')

    return render(request,'sign in.html')