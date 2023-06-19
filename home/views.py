from django.shortcuts import render,redirect

#
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')


def loginuser(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        # checking user creds
        user = authenticate(username=uname,password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request,'login.html')
    
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return render(request,'login.html')

def signinuser(request):
    if request.method == 'POST':
        uname=request.POST.get("uname")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        
        user = User.objects.create_user(uname,email,password)
        user.last_name = lname
        user.first_name = fname

        user.save()

        #
        login(request,user)
        return redirect('/')
    
    else:
        return render(request,'signup.html')