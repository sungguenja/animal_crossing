from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

app_name = 'community'
urlpatterns = [
    path('rescue/',views.rescue,name='rescue'),
    path('rescue/create/',views.rescue_create,name='rescue_create'),
    path('dealer/',views.dealer,name='dealer'),
    path('dealer/create/',views.dealer_create,name='dealer_create'),
    path('dealer/<int:article_pk>',views.detail,name='detail'),
    path('dealer/<int:article_pk>/state/',views.detail_state,name='detail_state')
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)