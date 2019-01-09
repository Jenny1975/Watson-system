from django.contrib import admin
from django.urls import path

from . import views

app_name = 'watsons'

urlpatterns = [
    path('', views.index, name='index'),
    path('RFM/chart', views.RFM_model, name='RFM'),
    path('RFM/list', views.RFM_model_list, name='RFM_list'),
    path('RFM/group', views.RFM_model_group, name='RFM_group'),
    path('breakeven/list', views.BreakEven, name='BreakEven'),
    path('breakeven/chart', views.BreakEven_chart, name='BreakEven_chart'),
    path('breakeven/edit', views.get_promotion, name='edit_BreakEven'),
    path('listall', views.listall, name='List all'),
    path('create', views.create, name='create'),
    path('show_transaction', views.showTransaction, name='showTransaction'),
    path('home/servive/', views.servive, name='servive'),        #存活率
    path('home/total_rate/', views.total_rate, name='total_rate'),  #個別錢包佔有率
    path('home/rate/', views.rate, name='rate'), 
    path('home', views.home, name='home'),     
]