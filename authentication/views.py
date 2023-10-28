from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.contrib import messages
from home.views import home_view


def login_view(request):
    if request.user.is_authenticated:
        return redirect(home_view)

    if request.method == 'POST':

        user_name = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            login(request, user)
            return redirect(home_view)
        else:
            messages.success(
                request, ("Invalid Credentials! If you don't have an account, Sign up!"))
            return redirect(login_view)

    return render(request, "login.html", context={})


def signup_view(request):

    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password1']
        bhawan = request.POST['bhawan']

        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            student = Student.objects.create(user=User.objects.create_user(
                username=user_name, password=password))
            student.bhawan = bhawan
            student.save()
            return redirect(login_view)

        else:

            messages.success(request, ("Invalid Credentials!"))
            return redirect(signup_view)

    return render(request, "signup.html", context={})


def logout_view(request):
    logout(request)
    return redirect(login_view)
