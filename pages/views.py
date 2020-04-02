from django.shortcuts import render

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
    pic = PhotoForm.objects.all()
    return render(request, 'pages/my_design.html')
