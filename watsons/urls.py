from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('chart', views.product_piechart, name='piechart'),
    path('detail', views.RFM_model, name='RFM')
]