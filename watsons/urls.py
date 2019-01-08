from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.RFM_model, name='RFM'),
    path('listall', views.listall, name='List all'),
    path('create', views.create, name='create'),
    path('show_transaction', views.showTransaction, name='showTransaction'),
]