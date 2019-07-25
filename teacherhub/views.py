from django.shortcuts import render_to_response, get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from chat.models import UserExtension

User = get_user_model()

def home_page(request):
    context = {}
    # context['']
    return render_to_response("home.html",context)

def login_(request):
    return render(request,'login.html')

def signup_(request):
    return render(request,'signup.html')

def login_post(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username=username,password=password) 
        if user:
            login(request,user)
            return render(request,'home.html')
        else:
            print('fail')

def signup_post(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user, created = User.objects.get_or_create(username=username,password=password)
        ue = UserExtension.objects.create(user=user)
        if created:
            login(request,user)
            return render(request,'home.html')
        else:
            render(request,'login.html')