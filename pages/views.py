import os
from django.apps import apps
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from random import choice
from .forms import *
from .models import *
import requests

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def nook(request):
    return render(request, 'pages/nook.html')

def villagers(request):
    neighbors = apps.get_model('accounts','Villagers').objects.prefetch_related('like_user').prefetch_related('live_with').order_by('kr_name')
    sp = ['dog','frog','Anteater','gorilla','cat','bear','wolf',
'squirrel','chicken','eagle','pig','horse','octopus','deer','lion','bird','cow','baby_bear','crocodile','sheep','goat','duck','monkey','mouse','kangaroo','eliphant','rhino','koala','ostrich','rabbit','penguin','hippo','hamster','tiger']
    context = {
        'neighbors':neighbors,
        'sp':sp
    }
    return render(request, 'pages/villagers.html', context)

def specy(request,spec):
    neighbors = apps.get_model('accounts','Villagers').objects.filter(species=spec).prefetch_related('like_user').prefetch_related('live_with').order_by('kr_name')
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
    neighbors = apps.get_model('accounts','Villagers').objects.filter(species=spec).prefetch_related('like_user').prefetch_related('live_with').order_by('kr_name')
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
            logined = True
            catch = False
            bug.catch_user.remove(request.user)
        else:
            logined = True
            catch = True
            bug.catch_user.add(request.user)
    else:
        logined = False
        catch = False
    return JsonResponse({'logined':logined,'catch':catch})

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
            logined = True
            catch = False
            fish.catch_user.remove(request.user)
        else:
            logined = True
            catch = True
            fish.catch_user.add(request.user)
    else:
        logined = False
        catch = False
    return JsonResponse({'logined':logined,'catch':catch})

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
        logined = True
        if this_design.like_users.filter(id=request.user.pk).exists():
            like = False
            this_design.like_users.remove(request.user)
        else:
            like = True
            this_design.like_users.add(request.user)
    else:
        logined = False
        like = False
    return JsonResponse({'logined':logined,'like':like})

def all_artwork(request):
    artworks = artwork.objects.all().order_by('title').prefetch_related('have_user')
    context = {
        'artworks': artworks
    }
    return render(request,'pages/artwork.html',context)

def have_artwork(request,artwork_id):
    if request.user.is_authenticated:
        this_artwork = get_object_or_404(artwork,pk=artwork_id)
        logined = True
        if this_artwork.have_user.filter(id=request.user.pk).exists():
            have = False
            this_artwork.have_user.remove(request.user)
        else:
            have = True
            this_artwork.have_user.add(request.user)
    else:
        have = False
        logined = False
    return JsonResponse({'logined':logined,'have':have})

def all_fossils(request):
    fossil_categories = fossil_category.objects.prefetch_related('fossil_set').order_by('title')
    context = {
        'fossil_categories': fossil_categories
    }
    return render(request,'pages/fossil.html',context)

def have_fossil(request,fossil_id):
    if request.user.is_authenticated:
        this_fossil = get_object_or_404(fossil,pk=fossil_id)
        logined = True
        if this_fossil.have_user.filter(pk=request.user.pk).exists():
            have = False
            this_fossil.have_user.remove(request.user)
        else:
            have = True
            this_fossil.have_user.add(request.user)
    else:
        logined = False
        have = False
    return JsonResponse({'logined':logined,'have':have})

def all_songs(request):
    songs = song.objects.order_by('kr_title')
    YOUTUBE_KEY = settings.YOUTUBE_KEY
    context = {
        'songs': songs,
        'key': YOUTUBE_KEY
    }
    return render(request,'pages/songs.html',context)

def have_song(request,song_id):
    if request.user.is_authenticated:
        logined = True
        this_song = get_object_or_404(song,pk=song_id)
        if this_song.have_user.filter(pk=request.user.pk).exists():
            have = False
            this_song.have_user.remove(request.user)
        else:
            have = True
            this_song.have_user.add(request.user)
    else:
        logined = False
        have = False
    return JsonResponse({'logined':logined,'have':have})