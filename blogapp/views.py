from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Category
from random import randint
from django.contrib.auth.decorators import login_required
from account.models import User
from django.contrib import auth
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
@staff_member_required
def getposts(request):
    current = request.user
    authorid = current.id
    if request.method == 'POST':
        # print("www")
        title = request.POST['title']
        content = request.POST['content']
        # author = request.POST['author']
        image = request.FILES['image']
        
        category = request.POST['category']
        # x = Category.objects.get(name=category)
        # if x:
        #     print(x.id)
        
        # breakpoint()
        post = Blog.objects.create(title=title,author_id= authorid,content=content,image=image,category_id=category)
        post.save()
        
        return redirect('blogs')

    return render(request,'getpost.html')
        
 


def blogs(request):

    posts = Blog.objects.all()
    count= Blog.objects.count()
    print(count)
    list=[]
    for i in range(3):
        list.append(randint((count-3),count))
    print(list)
   
    
    crousel1 = Blog.objects.get(id=list[0])
    crousel2 = Blog.objects.get(id=list[1])
    crousel3 = Blog.objects.get(id=list[2])
    

    return render(request,'home.html',{'posts':posts,'crousel1':crousel1,'crousel2':crousel2,'crousel3':crousel3})

def postdetail(request,pk):
    postshow = Blog.objects.get(id=pk)
    return render(request,'postdetail.html',{'postshow':postshow})

def index(request):
    # current = request.user
    # print(current.id)
    # print(current.name)

    
    return render(request,'index.html')
   
def logout(request):
    auth.logout(request)
    return redirect('/')

def getpostbycategory(request,cat):

    posts = Blog.objects.filter(category=cat)
    print(posts)
    count= Blog.objects.count()
    print(count)
    list=[]
    for i in range(3):
        list.append(randint((count-3),count))
    print(list)
   
    
    crousel1 = Blog.objects.get(id=list[0])
    crousel2 = Blog.objects.get(id=list[1])
    crousel3 = Blog.objects.get(id=list[2])
    

    return render(request,'bycategory.html',{'posts':posts,'crousel1':crousel1,'crousel2':crousel2,'crousel3':crousel3})


def userprofile(request):
    current_user = request.user
    print(current_user,current_user.email,current_user.name,current_user.phone,current_user.id)
    if request.method== 'POST':
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        renewpass = request.POST['renewpass']
        if current_user.check_password(oldpass) == True:
            if newpass == renewpass:
                current_user.set_password(newpass)
                current_user.save()
                return redirect('login')
            else:
                messages.info(request,"Password didn't match!!!")
        else:
                messages.info(request,"Please correctly insert your Old Password!!!")
    return render(request,'myprofile.html',{'current_user': current_user})

def updateprofile(request,pk):
    
    
    if request.method == 'POST':
        newname = request.POST['name']
        newphone = request.POST['phone']
        record = User.objects.get(id=pk)
        record.name = newname
        record.phone = newphone
        record.save()
        # newimage = request.File['image']
        messages.success(request, 'Your profile is updated successfully')
        return redirect('userprofile')
        print(record,record.name,record.phone)
        
    return render(request,'updateprofile.html')



def deleteprofile(request):
    current_user= request.user
    try:
        current_user.delete()
        return redirect('login')

    except:
        messages.info(request,"The user cannot be deleted")

   
def myblogs(request):
    current_user = request.user
    bloguserid = current_user.id
    posts = Blog.objects.filter(author_id = bloguserid)
    # print(posts,posts.content)
    return render(request, 'myblogs.html',{'current_user':current_user,'posts':posts})
     

def deleteblogs(request,pk):
    print(pk)
    blogtobedeleted = Blog.objects.get(id=pk)
    try:
        blogtobedeleted.delete()
        return redirect('myblogs')
    except:
        messages.info(request,"The blog cannot be deleted")
    
def editblogs(request,pk):
    print(pk)
    
    current = request.user
    authorid = current.id
    if request.method == 'POST':
        
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        category = request.POST['category']
        post = Blog.objects.get(id=pk)
        post.title= title
        post.content = content
        post.image = image
        post.category_id = category
        post.save()
        messages.success(request, 'Your profile is updated successfully')
        
        return redirect('myblogs')
        
  
        
    return render(request,'editblogs.html')
