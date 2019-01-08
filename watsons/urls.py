from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/servive/', views.servive, name='servive'),        #存活率
    path('home/total_rate/', views.total_rate, name='total_rate'),  #個別錢包佔有率
    path('home/rate/', views.rate, name='rate'),                 #錢包大小
    path('', views.home, name='home'),                           #主頁面
]