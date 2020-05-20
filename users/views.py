from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))
    
    return render(request, 'users/index.html', {})


def login_conform(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    print(user)
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'users/index.html', {
            'message': 'Invalid Credentials'
             })

def logout_view(request):
    logout(request)
    return render(request, 'users/index.html', {
        'message': 'Succesfully Logged out'
    })