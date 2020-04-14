from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .forms import *
from .models import *
import re
import os

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def nook(request):
    return render(request, 'pages/nook.html')

def villagers(request):
    now = []
    now = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, 'pages', 'static', 'villagers.txt')
    f = open(file_path, 'r', encoding='utf-8')
    gate=[]
    gate=[]

    for line, value in enumerate(f):
        gate.append(value[:-1])
        if line%7==6:
            gate[-1] = str(gate[0])+'.png'
            now.append(gate)
            gate=[]

    f.close()
    context = {
        'now': now
    }
    return render(request, 'pages/villagers.html', context)

def arr(request):
    return render(request, 'pages/arr.html')

def all_bug(request):

    now = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, 'pages', 'static', 'data.txt')
    f = open(file_path, 'r', encoding='utf-8')
    gate=[]

    for line, value in enumerate(f):
        if line>=568:
            break
        elif 6<line<568:
            if line%7==0:
                gate.append(re.sub('[^가-힣]','',value))
            elif line%7==1:
                gate.append(str(line//7)+'.png')
            elif line%7==2:
                gate.append(value[:-1])
            elif line%7==3:
                gate.append(value[:-1])
            elif line%7==4:
                gate.append(value[:-1])
            elif line%7==5:
                gate.append(value[:-1])
                now.append(gate)
                gate=[]
    f.close()
    context = {
        'now': now
    }

    return render(request, 'pages/bug.html', context)

def all_fish(request):
    now = []
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, 'pages', 'static', 'data1.txt')
    f = open(file_path, 'r', encoding='utf-8')
    gate=[]

    for line, value in enumerate(f):
        if line>=652:
            break
        elif 7<line<652:
            if line%8==0:
                gate.append(re.sub('[^가-힣]','',value))
            elif line%8==1:
                gate.append(str(line//8)+'.png')
            elif line%8==2:
                gate.append(value[:-1])
            elif line%8==3:
                gate.append(value[:-1])
            elif line%8==4:
                gate.append(value[:-1])
            elif line%8==5:
                gate.append(value[:-1])
            elif line%8==6:
                gate.append(value[:-1])
                now.append(gate)
                gate=[]
    f.close()
    context = {
        'now': now
    }

    return render(request, 'pages/fish.html', context)

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