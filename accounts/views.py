from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('pages:home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('pages:home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('pages:home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('pages:home')

@login_required
def profile(request,nickname):
    if nickname == '익명':
        messages.info(request,'죄송합니다 익명의 유저는 볼 수 없습니다')
        return redirect('pages:my_design')
    person = get_object_or_404(get_user_model(), nickname=nickname)
    bug_count = (int(person.catch_bug.count())/80)*100
    fish_count = (int(person.catch_fish.count())/80)*100
    context = {
        'person': person,
        'bug_count': bug_count,
        'fish_count': fish_count
    }
    return render(request,'accounts/profile.html', context)

@login_required
def follow(request,username):
    if username != request.user.username:
        person = get_object_or_404(get_user_model(), username=username)
        if person.followers.filter(id=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)

@login_required
def my_profile(request,user_id):
    if request.user.id != user_id:
        messages.info(request,'남의 프로필은 보실 수 없습니다')
        return redirect('pages:home')
    person = get_object_or_404(get_user_model(), id=user_id)
    bug_count = person.catch_bug.count()
    fish_count = person.catch_fish.count()
    context = {
        'person': person,
        'bug_count': bug_count,
        'fish_count': fish_count
    }
    return render(request,'accounts/profile.html', context)