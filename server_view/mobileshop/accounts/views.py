from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect("/")



def login(request):
    if request.method == "POST":  
        username = request.POST.get('username', '')  
        password = request.POST.get('password', '')  

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect("login")
    
    else:  
        return render(request, 'login.html')
         
    
    


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'User already exists')
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"the Email already exists")
                return redirect('register')
            else:

                user = User.objects.create_user(username=username,password=password1,first_name=first_name,email=email,last_name=last_name)
                user.save()
                print('user created')
                return redirect("login")
        else:
            messages.info("password not matching !!")
            return redirect('register')
    else:
        return HttpResponse(status=405)
        
    return redirect('/')
