from django.shortcuts import render, redirect
from . models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.


def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['pass']

        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        
        else:
            messages.info(request,'Invalid Email or Password!!!')

    
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass']
        repassword = request.POST['repass']

        if password == repassword:
            
            user = User.objects.create(name=name,email=email,phone=phone,password=password)
            user.set_password(password)
            
            user.save()
            return redirect('login')
        else:
            messages.info(request,"Password did't match, Please retype matching password!!")

        return render(request,'register.html')
            
    
    else:
        return render(request,'register.html')


    
    # return render(request,'register.html')



        

