from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from basicUserAuthApp.models import User
# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def index(request):
    return render(request,'basicUserAuthApp/index.html')
def login_page(request):
    return render(request,'basicUserAuthApp/login.html')
def registration(request):
    return render(request,'basicUserAuthApp/registration.html')
def user_page(request):
    return render(request,'basicUserAuthApp/user.html')
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Input Username:{username}")
        user = authenticate(username = username,password = password)
        if user:
            print("User is authenticated.")
            if user.is_active:
                print("User is active.")
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse(f"{username} account is not active")
        else:
            print("Someone tried to login, but fortunantly failed!")
            print(f"Username: {username}")
            return HttpResponse("Login is failed!")
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
        if password == reset_password:
            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            if user :
                print("User is registered!")
                print(f"User:{user}")
        else:
            return HttpResponse("Password typed differently!")
    print(f"Input First_name:{first_name}")
    print(f"Input Last_name:{last_name}")
    print(f"Input Username:{username}")
    print(f"Input Email:{email}")
    print(f"Status password{password == reset_password}")
    return index(request)
