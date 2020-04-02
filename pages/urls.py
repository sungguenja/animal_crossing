from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('nook/', views.nook),
    path('villagers/', views.villagers),
    path('arr/', views.arr),
    path('my_design/', views.my_design),
]