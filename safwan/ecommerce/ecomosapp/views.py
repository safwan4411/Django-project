from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutview(request):
    return render(request,'about.html')

def registerview(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

