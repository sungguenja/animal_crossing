from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:nickname>/', views.profile, name='profile'),
    path('<str:nickname>/follow/', views.follow, name='follow'),
    path('<int:user_id>/my_profile/',views.my_profile,name='my_profile')
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)