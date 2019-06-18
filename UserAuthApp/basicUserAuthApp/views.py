from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from basicUserAuthApp import models
# Create your views here.
def index(request):
    return render(request,'basicUserAuthApp/index.html')
def login(request):
    return render(request,'basicUserAuthApp/login.html')
def registration(request):
    return render(request,'basicUserAuthApp/registration.html')
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    print(username)
    return index(request)
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reset_password = request.POST.get('rest_password')
    print(first_name)
    print(last_name)
    print(username)
    print(email)
    return index(request)
