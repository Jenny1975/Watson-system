from django.contrib import admin
from django.urls import path

from . import views

app_name = 'watsons'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('show_transaction', views.showTransaction, name='showTransaction'),



]