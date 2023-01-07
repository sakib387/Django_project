from django.shortcuts import render,HttpResponseRedirect
from .forms import SinUpForm,LoginForm,PostForm
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def home(request):
    post=Post.objects.all()
    return render(request,'home.html',{'post':post})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    if   request.user.is_authenticated:
     posts=Post.objects.all()
     user=request.user
     full_name=user.get_full_name()
     gps=user.groups.all()
     return render(request,'dashboard.html',{'post':posts,'full_name':full_name,'group':gps})
    else:
        return HttpResponseRedirect('/login')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home')

def user_sinup(request):
    if request.method == "POST":
        form=SinUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'congratulations !! You are welcome ')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
            
    else:
     form=SinUpForm()
    return render(request,'sinup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method =="POST":
            
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
            
                unm=form.cleaned_data['username']
                ups=form.cleaned_data['password']
                
                user=authenticate(username=unm,password=ups)
                print(user)
                if user is not None:
                    
                    login(request,user)
                    messages.success(request,'wellcome')
                    return HttpResponseRedirect('/dashboard/',{'unm':unm})
        else :
         form=LoginForm()
        return render(request,'login.html',{'form':form})
    else :
        return HttpResponseRedirect('/dashboard/')
    
    
def add_post(request):
     if  request.user.is_authenticated:
         if request.method =='POST':
          form=PostForm(request.POST)
          if form.is_valid():
           form.save()
         else :
             form=PostForm() 
         return render(request,'addpost.html',{'form':form})
     else:
         return HttpResponseRedirect('/login/')
     
def update_post(request,id):
     if  request.user.is_authenticated:
         if request.method=='POST':
              pi=Post.objects.get(pk=id)
              form=PostForm(request.POST,instance=pi)
              if form.is_valid():
                  form.save()
         else:
            pi=Post.objects.get(pk=id)
            form=PostForm(instance=pi)
                  
              
         return render(request,'updatepost.html',{'form':form})
     else:
         return HttpResponseRedirect('/login/')
 
 
def delete_post(request,id):
     if  request.user.is_authenticated:
         if request.method=='POST':
             pi=Post.objects.get(pk=id)
             pi.delete()
         return HttpResponseRedirect('/dashboard/')
     else:
         return HttpResponseRedirect('/login/')
 