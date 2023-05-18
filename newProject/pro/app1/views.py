from django.shortcuts import render
from django.contrib.auth import forms
from app1.form import bookForm
from app1.models import books
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def base(request):
    return render(request,'base.html')



def upload(request):
    form=bookForm()
    if(request.method=="POST"):
        form=bookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return base(request)
    return render(request,'upload.html',{'form':form})



def showbooks(request):
    k=books.objects.all()
    return render(request,'showbooks.html',{"s":k})


def delete_book(request,p):
    s=books.objects.get(pk=p)
    s.delete()
    return showbooks(request)
     

def edit_book(request,p):
    d=books.objects.get(pk=p)
    form=bookForm(instance=d)
    if (request.method=='POST'):
         form=bookForm(request.POST,instance=d)
         if(form.is_valid()):
              form.save()
              return showbooks(request)
    return render(request,'upload.html',{'form':form})

def search(request):
    if(request.method=="POST"):
        srch=request.POST['search']
        if srch:
            match=books.objects.filter(Q(title__icontains=srch)|Q(author__icontains=srch))
            if match:
                return render(request,'search.html',{'s':match})
            else:
                return search(request)
        else:
            messages.error(request,'no result found')

    return render(request,'search.html')