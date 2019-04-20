from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(email=request.POST['email'])
                return render(request, 'accounts/signup.html', {'err': 'This email already exists.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['user_name'], email=request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'err': 'Passwords do not match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = get_object_or_404(User, email=request.POST['email']).username
        user = auth.authenticate(username=username, password=request.POST['password'])
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'err': 'Email or Password is Incorrect!'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
