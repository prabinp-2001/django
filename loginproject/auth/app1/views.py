from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from app1.form import auth
from app1.form import authForm
from app1.form import CustomUserCreationForm
from app1.form import employeeForm
from app1.models import Employee

# Create your views here.

def home(request):
    return render(request,'index.html')

def mainpage(request):
    return render(request,'mainpage.html')

def about(request):
    return render(request,'about.html')



# def signup(request):
#     form=UserCreationForm()
#     if (request.method=='POST'):
#         form=UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return mainpage(request)
#     return render(request,'signup.html',{"form":form})

def user_login(request):
    if(request.method =='POST'):
                name=request.POST['n']
                password=request.POST['p']
                user = authenticate(username=name, password=password)
                if user:
                    login(request,user)
                    return mainpage(request)
                else:
                    return HttpResponse('invalid user')
        
    return render(request,'login1.html')

def logout1(request):
    logout(request)
    return user_login(request)

# def signup(request):
#     form=authForm()
#     if (request.method=='POST'):
#         form=authForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return home(request)
#     return render(request,'signup.html',{"form":form})



def signup(request):
    form=CustomUserCreationForm()
    if (request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return mainpage(request)
    return render(request,'signup.html',{"form":form})






def add(request):
    form=employeeForm()
    if request.method=='POST':
        form=employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return view(request)
    return render(request,'add.html',{'form':form})



def view(request):
     k=Employee.objects.all()
     return render(request,'view.html',{'p':k})

def delete_emp(request,p):
     s=Employee.objects.get(pk=p)
     s.delete()
     return view(request)

def edit_emp(request,p):
    d=Employee.objects.get(pk=p)
    form=employeeForm(instance=d)
    if (request.method=='POST'):
         form=employeeForm(request.POST,instance=d)
         if(form.is_valid()):
              form.save()
              return view(request)
    return render(request,'add.html',{'form':form})
     