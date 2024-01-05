from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/")
def registerpage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username Already Taken.", extra_tags="danger")
            return redirect('/')


        user = User.objects.create  (
            email = email,
            username  = username
        )
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account Created Sucessfully!")

        return redirect('/home/')
    return render(request, "signup.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username", extra_tags="danger")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password", extra_tags="danger")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')

    return render(request, "login.html")

@login_required(login_url="/login/")
def logoutpage(request):
    logout(request)
    return redirect('/login/')

def home(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        en = Student(
            name = name,
            age = age,
            email = email,
            phone = phone,
            address = address
        )
        en.save()
        return redirect('/home')
    queryset = Student.objects.all()

    # if request.GET.get('search'):
    #     queryset = queryset.filter(name__icontains = request.GET.get('search'))

    context = {'Student':queryset}
    
    return render(request, "form.html",context)
def delete_data(request,id):
    queryset = Student.objects.get(id = id)
    queryset.delete()
    return redirect('/home')
def update_data(request,id):
    queryset = Student.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        
        queryset.name = name
        queryset.age = age
        queryset.email = email
        queryset.phone = phone
        queryset.address = address

        queryset.save()
        return redirect('/home')
    context = {'Student':queryset}
    return render(request, "updated.html",context)
