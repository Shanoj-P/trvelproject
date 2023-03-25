from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':
        username= request.POST['UserName']
        firstname = request.POST['FirstName']
        lastname = request.POST['LastName']
        email = request.POST['Email']
        password = request.POST['Password']
        cpassword = request.POST['password1']
        if password== cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, password=password, email=email, first_name= firstname, last_name= lastname)

                user.save();
                return redirect('login')

                print("user created")

        else:
            messages.info(request,"Password does not match")
            return redirect('register')
            print("Password does not match")
        return redirect('/')
    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
