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
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, 'pages', 'static', 'villagers.txt')
    f = open(file_path, 'r', encoding='utf-8')
    gate=[]
    trigger = 'dog'
    dogs = []
    frogs = []
    anteaters = []
    gorilas = []
    cats = []
    bears = []
    wolves = []
    squirrel = []
    chickens = []
    eagles = []
    pigs = []
    horses = []
    tacos = []
    deers = []
    lions = []
    birds = []
    cows = []
    littlebear = []
    elligator = []
    sheep = []
    goats = []
    ducks = []
    monkeys = []
    mice = []
    kangaroos = []
    eliphants = []
    Rhinoceros = []
    koalas = []
    ostriches = []
    rabbits = []
    penguins = []
    hippos = []
    hamseters = []
    tigers = []

    for line, value in enumerate(f):
        gate.append(value[:-1])
        if line%7==6:
            gate[-1] = str(gate[0])+'.png'
            now.append(gate)
            if trigger == 'dog':
                dogs.append(gate)
                if gate[0] == '밥':
                    trigger = 'frog'
            elif trigger == 'frog':
                frogs.append(gate)
                if gate[0] == '헨리':
                    trigger = '개미핥기'
            elif trigger == '개미핥기':
                anteaters.append(gate)
                if gate[0] == '안토니오':
                    trigger = 'gorilla'
            elif trigger == 'gorilla':
                gorilas.append(gate)
                if gate[0] == '릴라':
                    trigger = 'cat'
            elif trigger == 'cat':
                cats.append(gate)
                if gate[0] == '잭슨':
                    trigger = 'bear'
            elif trigger == 'bear':
                bears.append(gate)
                if gate[0] == '캔디':
                    trigger = 'wolf'
            elif trigger == 'wolf':
                wolves.append(gate)
                if gate[0] == '모니카':
                    trigger = 'squ'
            elif trigger == 'squ':
                squirrel.append(gate)
                if gate[0] == '미사키':
                    trigger = 'chickens'
            elif trigger == 'chickens':
                chickens.append(gate)
                if gate[0] == '오골':
                    trigger = 'eagle'
            elif trigger == 'eagle':
                eagles.append(gate)
                if gate[0] == '티파니':
                    trigger = 'pig'
            elif trigger == 'pig':
                pigs.append(gate)
                if gate[0] == '가논':
                    trigger = 'horse'
            elif trigger == 'horse':
                horses.append(gate)
                if gate[0] == '리아나':
                    trigger = 'taco'
            elif trigger == 'taco':
                tacos.append(gate)
                if gate[0] == '멍무리':
                    trigger = 'deer'
            elif trigger == 'deer':
                deers.append(gate)
                if gate[0] == '첼시':
                    trigger = 'lion'
            elif trigger == 'lion':
                lions.append(gate)
                if gate[0] == '라이오넬':
                    trigger = 'bird'
            elif trigger == 'bird':
                birds.append(gate)
                if gate[0] == '메들리':
                    trigger='cow'
            elif trigger == 'cow':
                cows.append(gate)
                if gate[0] == '화자':
                    trigger = 'lb'
            elif trigger == 'lb':
                littlebear.append(gate)
                if gate[0] == '미애':
                    trigger = 'eg'
            elif trigger == 'eg':
                elligator.append(gate)
                if gate[0] == '용남이':
                    trigger = 'sheep'
            elif trigger == 'sheep':
                sheep.append(gate)
                if gate[0] == '차둘':
                    trigger = 'goat'
            elif trigger == 'goat':
                goats.append(gate)
                if gate[0] == '래미':
                    trigger = 'goose'
            elif trigger == 'goose':
                ducks.append(gate)
                if gate[0] == '덕근':
                    trigger = 'monkey'
            elif trigger == 'monkey':
                monkeys.append(gate)
                if gate[0] == '델리':
                    trigger = 'mouse'
            elif trigger == 'mouse':
                mice.append(gate)
                if gate[0] == '치즈':
                    trigger = 'kang'
            elif trigger == 'kang':
                kangaroos.append(gate)
                if gate[0] == '마리아':
                    trigger = 'elip'
            elif trigger == 'elip':
                eliphants.append(gate)
                if gate[0] == '펑크스':
                    trigger = 'rino'
            elif trigger == 'rino':
                Rhinoceros.append(gate)
                if gate[0] == '뿔님이':
                    trigger = 'koal'
            elif trigger == 'koal':
                koalas.append(gate)
                if gate[0] == '코알':
                    trigger = 'ostric'
            elif trigger == 'ostric':
                ostriches.append(gate)
                if gate[0] == '휘니':
                    trigger = 'rabbit'
            elif trigger == 'rabbit':
                rabbits.append(gate)
                if gate[0] == '토비':
                    trigger = 'peng'
            elif trigger == 'peng':
                penguins.append(gate)
                if gate[0] == '크리미':
                    trigger = 'hippo'
            elif trigger == 'hippo':
                hippos.append(gate)
                if gate[0] == '데이빗':
                    trigger = 'ham'
            elif trigger == 'ham':
                hamseters.append(gate)
                if gate[0] == '햄쥐':
                    trigger = 'tiger'
            elif trigger == 'tiger':
                tigers.append(gate)
            gate=[]

    f.close()
    context = {
        'now': now,
        'dogs': dogs,
        'frogs': frogs,
        'anteaters': anteaters,
        'gorilas': gorilas,
        'cats': cats,
        'bears': bears,
        'wolves': wolves,
        'squirrel': squirrel,
        'chickens': chickens,
        'eagles': eagles,
        'pigs': pigs,
        'horses': horses,
        'tacos': tacos,
        'deers': deers,
        'lions': lions,
        'birds': birds,
        'cows': cows,
        'littlebear': littlebear,
        'elligator': elligator,
        'sheep': sheep,
        'goats': goats,
        'ducks': ducks,
        'monkeys': monkeys,
        'mice': mice,
        'kangaroos': kangaroos,
        'eliphants': eliphants,
        'Rhinoceros': Rhinoceros,
        'koalas': koalas,
        'ostriches': ostriches,
        'rabbits': rabbits,
        'penguins': penguins,
        'hippos': hippos,
        'hamseters': hamseters,
        'tigers': tigers
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
            form = Design_Form(request.POST, request.FILES, request.POST)
            
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