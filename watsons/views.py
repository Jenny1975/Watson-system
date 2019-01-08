from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
import json
#import numpy as np
#import pandas as pd
from .models import Customer,Transaction,Product,Pocket_other,Servive
import matplotlib.pyplot as plt


from .models import Transaction, Product, Customer


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_transaction_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Transaction.objects.order_by('-time')[:5]


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'detail.html'


###below are modified

def servive(request): #存活率
    ser = Servive.objects.order_by('Date')
    r = 1
    n = 100
    period = 0
    day=[]
    se=[]
    for s in ser:
        s.count((s.Num/n), r)
        r = s.servive_rate
        n = s.Num
        period = period+s.respected_customer_num
        day.append(s.Date)
        se.append(r)
    plt.plot(day, se)
    plt.title('Survival rate Graph')
    plt.ylabel('Date')
    plt.xlabel('servive rate')
    plt.show()
    period = period/100
    context = {'ser': ser, 'period': period, }
    return render(request, 'servive.html', context)


def total_rate(request): #個別錢包佔有率
    poc = Pocket_other.objects.order_by('customer').all()
    poc2 = Pocket_other.objects.order_by('customer')
    cal_rate(poc, poc2)
    context = {'poc2': poc2}
    return render(request, 'total_rate.html', context)


def rate(request):  #錢包大小
    poc = Pocket_other.objects.order_by('customer').all()
    dict1 = cal_poc(poc)
    context = {'poc': poc}
    context.update(dict1)
    return render(request, 'rate.html', context)


def cal_poc(poc):  #call function  from  rate,total_rate
    cosmetic = 0
    snacks = 0
    care = 0
    for p in poc:
        p.total_Cosmetic = p.total_Cosmetic*40
        p.total_Snacks = p.total_Snacks*200
        p.total_Care = p.total_Care*120
        cosmetic = cosmetic + p.total_Cosmetic
        snacks = snacks + p.total_Snacks
        care = care + p.total_Care
    dict1 = {'cosmetic': cosmetic, 'snacks': snacks, 'care': care}
    return dict1



 # call function  from  total_rate
def cal_rate(poc1,poc2):
    cost = Customer.objects.order_by('customer_name').all()
    for c in cost:
        tran = Transaction.objects.order_by('customer').filter(customer_id=c.id)   # 找到顧客交易資料
        p = poc2.filter(customer_id=c.id)
        p1 = poc1.filter(customer_id=c.id)                                         # poc1 為此顧客的錢包大小
        p.total_Cosmetic = 0
        p.total_Snacks = 0
        p.total_Care = 0
        for t in tran:                                                             # 找到的交易資訊 依據品類統計
            pro = Product.objects.filter(product_name=t.product)
            if pro.category == 'Cosmetic':
                p.total_Cosmetic = p.total_Cosmetic+t.total
            elif pro.category == 'Snacks':
                p.total_Snacks = p.total_Snacks + t.total
            elif pro.category == 'Care Product':
                p.total_Care = p.total_Care + t.total
        p.total_Cosmetic = p.total_Cosmetic/p1.total_Cosmetic                     # 算出顧客在各品類的錢包佔有率
        p.total_Snacks = p.total_Snacks/p1.total_Snacks
        p.total_Care = p.total_Care/p1.total_Care



def home(request): #首頁

    return render(request, 'home.html', locals())
    





