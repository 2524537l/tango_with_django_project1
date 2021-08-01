from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html',{'hello':"Rango says hey there partner!"})

def about(request):
    return render(request,'about.html',{'hellow':"Rango says here is the about page."})

