from django.shortcuts import render,redirect

#
from django.contrib.auth import authenticate , login
from django.contrib.auth import logout

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
    return render(request,'logout.html')

def signinuser(request):
    return render(request,'signup.html')

    # return redirect('/login')