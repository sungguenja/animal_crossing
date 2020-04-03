from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.home),
    path('nook/', views.nook),
    path('villagers/', views.villagers),
    path('arr/', views.arr),
    path('my_design/', views.my_design),
    path('my_design/your_design/', views.your_design),
    path('my_design/affect/', views.your_design),
    path('my_design/success/', views.success),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)