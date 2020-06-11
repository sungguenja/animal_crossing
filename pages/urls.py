from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('nook/', views.nook, name='nook'),
    path('villagers/', views.villagers, name='villagers'),
    path('villagers/random/', views.vil_ran, name='vil_ran'),
    path('villagers/<str:spec>/', views.specy, name='spec'),
    path('<int:villager_id>/like/',views.like,name='like'),
    path('<int:villager_id>/live/',views.live,name='live'),
    path('arr/', views.arr, name='arr'),
    path('arr/bugs/', views.all_bug, name='all_bug'),
    path('arr/bugs/<int:bug_id>/', views.catch_bug, name='catch_bug'),
    path('arr/fishes/', views.all_fish, name='all_fish'),
    path('arr/fishes/<int:fish_id>/', views.catch_fish, name='catch_fish'),
    path('arr/artworks/',views.all_artwork,name='all_artwork'),
    path('arr/artworks/<int:artwork_id>/',views.have_artwork,name='have_artwork'),
    path('my_design/', views.my_design, name='my_design'),
    path('my_design/affect/', views.your_design, name='your_design'),
    path('my_design/<int:design_id>/', views.like_design, name='like_design'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)