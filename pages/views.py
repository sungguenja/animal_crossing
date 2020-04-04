from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def nook(request):
    return render(request, 'pages/nook.html')

def villagers(request):
    return render(request, 'pages/villagers.html')

def arr(request):
    return render(request, 'pages/arr.html')

def my_design(request):
    if request.method == 'GET':
        pic = design.objects.all()
        pic = pic[::-1]
        context = {
            'pic': pic
        }
        return render(request, 'pages/my_design.html', context)

def your_design(request):
    if request.method == 'POST':
        form = Design_Form(request.POST, request.FILES, request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/wiki_like/my_design/')
    else:
        form = Design_Form()
    return render(request, 'pages/affect.html', {'form': form})

def affect(request):
    return render(request,'pages/affect.html')

def success(request): 
    return HttpResponse('successfully uploaded') 