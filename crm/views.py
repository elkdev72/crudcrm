from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return render(request,"index.html")


def logout_view(request):
    logout(request)
    return redirect("/")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html",{"error":"Invalid username or password"})

    return render(request,"login.html") 

def register_view(request):
    if request.method == "POST":
        first_name =first_name
        last_name = last_name
        username = username
        email = email
        password = password
        confirm_password = confirm_password

        if password == confirm_password:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            return redirect("/")
        else:
            return render(request,"register.html",{"error":"Passwords do not match"})

    return render(request,"register.html")