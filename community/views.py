from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .models import *
from .forms import *

# Create your views here.
now = datetime.datetime.now()
def rescue(request):
    radishes = Radish.objects.filter(start__lte=now).filter(end__gte=now).order_by('bell')
    context = {'radishes':radishes}
    return render(request,'community/radishes.html',context)

def rescue_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Radish_Form(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('community:rescue')
        else:
            form = Radish_Form()
        return render(request,'community/create.html',{'form':form})
    else:
        return redirect('community:rescue')

def dealer(request):
    sort = request.GET.get('sort','')
    if sort != '':
        articles = Article.objects.filter(soldout=0,category=sort).order_by('-pk')
    else:
        articles = Article.objects.filter(soldout=0).order_by('-pk')
    context = {'articles':articles}
    return render(request,'community/dealer.html',context)

def dealer_create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Article_Form(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.user = request.user
                article.save()
                return redirect('community:dealer')
        else:
            form = Article_Form()
        return render(request,'community/create.html',{'form':form})
    else:
        return redirect('community:dealer')

def detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    context = {'article':article}
    return render(request,'community/detail.html',context)

def detail_state(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    if article.user == request.user:
        article.soldout = (article.soldout+1)%2
        article.save()
    return redirect('community:detail',article_pk)