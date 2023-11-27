from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('passwd')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            firstname=user.first_name            
            return render(request,'dashboard.html',{'firstname':firstname})
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

            # return redirect('/login')
    return render(request,'login.html')

def create(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password=request.POST['passwd']
        email=request.POST['email']
      
        userdata=User.objects.create_user(username=username,email=email,password=password)
        userdata.last_name=lastname
        userdata.first_name=firstname
        
        userdata.save()
        
        messages.success(request,'User created successfully')
        
        return redirect('/login')
    return render(request,'create.html')


def dashboard(request):
    return render(request,'dashboard.html')