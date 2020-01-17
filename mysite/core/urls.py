# from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.urls import *
from . models import Apps
from . import views
# app_name='core'
urlpatterns = [    
    path('signup/', views.signup, name='signup'),    
    path('', views.home, name='home'),
    # path('secret/', views.secret_page, name='secret'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),    
    path('accounts/', include('django.contrib.auth.urls')),
    path('<int:apps_id>/entrainements/', views.entrainements, name='entrainements'),
]