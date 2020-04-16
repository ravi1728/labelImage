from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def label(request):
    return render(request,'label.html')