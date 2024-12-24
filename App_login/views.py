from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()  # No need to call set_password
            return render(request, 'auth/register_done.html', {'new_user': new_user})
        else:
            # Provide feedback if the form is invalid
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('App_login:login')  # Redirect to the login page within the namespace
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'auth/login.html')  # Render the login template

def logout(request):
    auth.logout(request)  # Logs out the user
    messages.success(request, 'You have successfully logged out!')
    return redirect('App_login:login')

