import os
from django.apps import apps
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from random import choice
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def nook(request):
    return render(request, 'pages/nook.html')

def villagers(request):
    neighbors = apps.get_model('accounts','Villagers').objects.prefetch_related('like_user').prefetch_related('live_with').all()
    sp = ['dog','frog','Anteater','gorilla','cat','bear','wolf',
'squirrel','chicken','eagle','pig','horse','octopus','deer','lion','bird','cow','baby_bear','crocodile','sheep','goat','duck','monkey','mouse','kangaroo','eliphant','rhino','koala','ostrich','rabbit','penguin','hippo','hamster','tiger']
    context = {
        'neighbors':neighbors,
        'sp':sp
    }
    return render(request, 'pages/villagers.html', context)

def specy(request,spec):
    neighbors = apps.get_model('accounts','Villagers').objects.filter(species=spec).prefetch_related('like_user').prefetch_related('live_with')
    sp = ['dog','frog','Anteater','gorilla','cat','bear','wolf',
'squirrel','chicken','eagle','pig','horse','octopus','deer','lion','bird','cow','baby_bear','crocodile','sheep','goat','duck','monkey','mouse','kangaroo','eliphant','rhino','koala','ostrich','rabbit','penguin','hippo','hamster','tiger']
    context = {
        'neighbors':neighbors,
        'sp':sp
    }
    return render(request, 'pages/villagers.html', context)

def vil_ran(request):
    sp = ['dog','frog','Anteater','gorilla','cat','bear','wolf',
'squirrel','chicken','eagle','pig','horse','octopus','deer','lion','bird','cow','baby_bear','crocodile','sheep','goat','duck','monkey','mouse','kangaroo','eliphant','rhino','koala','ostrich','rabbit','penguin','hippo','hamster','tiger']
    spec = choice(sp)
    neighbors = apps.get_model('accounts','Villagers').objects.filter(species=spec).prefetch_related('like_user').prefetch_related('live_with')
    context = {
        'neighbors':neighbors,
        'sp':sp
    }
    return render(request, 'pages/villagers.html', context)

def like(request,villager_id):
    if request.user.is_authenticated:
        neighbor = get_object_or_404(apps.get_model('accounts','Villagers'),id=villager_id)
        if neighbor.like_user.filter(id=request.user.pk).exists():
            logined = True
            liked = False
            neighbor.like_user.remove(request.user)
        else:
            logined = True
            liked = True
            neighbor.like_user.add(request.user)
    else:
        logined = False
        liked = True
    return JsonResponse({'logined':logined,'liked':liked})

def live(request,villager_id):
    if request.user.is_authenticated:
        neighbor = get_object_or_404(apps.get_model('accounts','Villagers'),id=villager_id)
        if neighbor.live_with.filter(id=request.user.pk).exists():
            neighbor.live_with.remove(request.user)
            logined = True
            lived = False
            ten = False
        else:
            if request.user.live_villager.count() < 10:
                neighbor.live_with.add(request.user)
                logined = True
                lived = True
                ten = False
            else:
                logined = True
                lived = False
                ten = True
    else:
        logined = False
        lived = False
        ten = False
    return JsonResponse({'logined':logined,'lived':lived,'ten':ten})

def arr(request):
    return render(request, 'pages/arr.html')

def all_bug(request):
    bugs = apps.get_model('accounts','Bug').objects.all().prefetch_related('catch_user')
    context = {
        'bugs':bugs
    }

    return render(request, 'pages/bug.html', context)

def catch_bug(request,bug_id):
    if request.user.is_authenticated:
        bug = get_object_or_404(apps.get_model('accounts','Bug'),id=bug_id)
        if bug.catch_user.filter(id=request.user.pk).exists():
            bug.catch_user.remove(request.user)
        else:
            bug.catch_user.add(request.user)
    else:
        messages.warning(request,'로그인을 해주시길 바랍니다.')
    return redirect('pages:all_bug')

def all_fish(request):
    fishes = apps.get_model('accounts','Fish').objects.all().prefetch_related('catch_user')
    context = {
        'fishes':fishes
    }

    return render(request, 'pages/fish.html', context)

def catch_fish(request,fish_id):
    if request.user.is_authenticated:
        fish = get_object_or_404(apps.get_model('accounts','Fish'),id=fish_id)
        if fish.catch_user.filter(id=request.user.pk).exists():
            fish.catch_user.remove(request.user)
        else:
            fish.catch_user.add(request.user)
    else:
        messages.warning(request,'로그인을 해주시길 바랍니다.')
    return redirect('pages:all_fish')

def my_design(request):
    pic = design.objects.prefetch_related('like_users').all()
    pic = pic[::-1]
    top = []
    onepiece = []
    hat = []
    no_cat = []
    for i in pic:
        if i.category == '상의':
            top.append(i)
        elif i.category == '원피스':
            onepiece.append(i)
        elif i.category == '모자':
            hat.append(i)
        elif i.category == '분류X':
            no_cat.append(i)
        
    context = {
        'pic': pic,
        'hat': hat,
        'onepiece': onepiece,
        'top': top,
        'no_cat': no_cat
    }
    return render(request, 'pages/my_design.html', context)

def your_design(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Design_Form(request.POST, request.FILES)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('pages:my_design')
        else:
            form = Design_Form()
        return render(request, 'pages/affect.html', {'form': form})
    else:
        return redirect('pages:my_design')

def like_design(request,design_id):
    if request.user.is_authenticated:
        this_design = get_object_or_404(design,id=design_id)
        if this_design.like_users.filter(id=request.user.pk).exists():
            this_design.like_users.remove(request.user)
        else:
            this_design.like_users.add(request.user)
    else:
        messages.warning(request,'로그인을 해주시길 바랍니다.')
    return redirect('pages:my_design')