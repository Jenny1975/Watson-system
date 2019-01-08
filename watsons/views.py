from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
# from django.urls import reverse
# from django.http import JsonResponse
# import json
# import numpy as np 
# import pandas as pd
# import matplotlib.pyplot as plt
# from pylab import figure, axes, pie, title
# from matplotlib.backends.backend_agg import FigureCanvasAgg

from .models import Transaction, Product, Customer



def index(request):
    latest_transaction_list = Transaction.objects.order_by('-time')[:5]
    context = {'latest_transaction_list': latest_transaction_list}
    return render(request, 'watsons/index.html', context)




#RFM Model start
def RFM_model(request):
    customer_list = Customer.objects.all()

    customer_transaction_list = []

    for cm in customer_list:
        transaction_queryset = cm.transaction_set.order_by('delta_date')
        customer_transaction_list.append({"Customer": cm, "Transaction_Query": transaction_queryset})
    
    for customer_t in customer_transaction_list:
        customer_t["recent_num"] = create_recent_number(customer_t["Transaction_Query"])
        customer_t["frequency_num"] = create_frequency_number(customer_t["Transaction_Query"])
        customer_t["amount_num"] = create_amount_number(customer_t["Transaction_Query"])
        customer_t["average_spending"] = customer_avg(customer_t["Transaction_Query"])

    recent_avg_list = calculate_avg(customer_transaction_list, 1)
    frequency_avg_list = calculate_avg(customer_transaction_list, 2)
    amount_avg_list = calculate_avg(customer_transaction_list, 3)



    
    dataset_recent = [{'recent': 5, 'recent_average_amount': recent_avg_list[4]},
                {'recent': 4, 'recent_average_amount': recent_avg_list[3]},
                {'recent': 3, 'recent_average_amount': recent_avg_list[2]},
                {'recent': 2, 'recent_average_amount': recent_avg_list[1]},
                {'recent': 1, 'recent_average_amount': recent_avg_list[0]}]

    dataset_frequency = [{'frequency': 5, 'frequency_average_amount': frequency_avg_list[4]},
                {'frequency': 4, 'frequency_average_amount': frequency_avg_list[3]},
                {'frequency': 3, 'frequency_average_amount': frequency_avg_list[2]},
                {'frequency': 2, 'frequency_average_amount': frequency_avg_list[1]},
                {'frequency': 1, 'frequency_average_amount': frequency_avg_list[0]}]
                
    dataset_amount = [{'amount': 5, 'amount_average_amount': amount_avg_list[4]},
                {'amount': 4, 'amount_average_amount': amount_avg_list[3]},
                {'amount': 3, 'amount_average_amount': amount_avg_list[2]},
                {'amount': 2, 'amount_average_amount': amount_avg_list[1]},
                {'amount': 1, 'amount_average_amount': amount_avg_list[0]},]


    return render(request, 'watsons/detail.html', {'dataset_recent': dataset_recent,
                                                'dataset_frequency': dataset_frequency, 
                                                'dataset_amount' : dataset_amount})


def customer_avg(customer_query):
    total = 0
    count = 0
    for c in customer_query:
        total += c.transaction_total
        count += 1
    average = total / count

    return average


def calculate_avg(list, attribute):
    count_5 = 0
    count_4 = 0
    count_3 = 0
    count_2 = 0
    count_1 = 0
    total_5 = 0
    total_4 = 0
    total_3 = 0
    total_2 = 0
    total_1 = 0
    customer_transaction_list = list
        
    
    for customer in customer_transaction_list:
        if attribute == 1:
            at = customer["recent_num"]
        elif attribute == 2:
            at = customer["frequency_num"]
        else:
            at = customer["amount_num"]

        customer_total = customer["average_spending"]
        if at == 5:
            count_5 += 1
            total_5 += customer_total
        elif at == 4:
            count_4 += 1
            total_4 += customer_total
        elif at == 3:
            count_3 += 1
            total_3 += customer_total
        elif at == 2:
            count_2 += 1
            total_2 += customer_total
        else:
            count_1 += 1
            total_1 += customer_total
    
    average_5 = total_5 / count_5
    average_4 = total_4 / count_4
    average_3 = total_3 / count_3
    average_2 = total_2 / count_2
    average_1 = total_1 / count_1

    return [average_1, average_2, average_3, average_4, average_5]

def create_recent_number(list):
    customer_recent_transaction = list[0]
    recent_day = customer_recent_transaction.delta_date
    if recent_day < 7:
        recent_num = 5
    elif recent_day < 15:
        recent_num = 4
    elif recent_day < 22:
        recent_num = 3
    elif recent_day < 29:
        recent_num = 2
    else:
        recent_num = 1
    return recent_num

def create_frequency_number(list):
    customer_first_transaction = list.reverse()[0]
    first_day = customer_first_transaction.delta_date
    count = 0
    for i in list:
        count += 1
    frquency_day = first_day / count
    if frquency_day < 4:
        frquency_num = 5
    elif frquency_day < 7:
        frquency_num = 4
    elif frquency_day < 10:
        frquency_num = 3
    elif frquency_day < 14:
        frquency_num = 2
    else:
        frquency_num = 1
    return frquency_num


def create_amount_number(list):
    recent_transaction = list [0]
    recent_amount = recent_transaction.transaction_total
    if recent_amount > 1000:
        amount_num = 5
    elif recent_amount > 500:
        amount_num = 4
    elif recent_amount > 300:
        amount_num = 3
    elif recent_amount > 100:
        amount_num = 2
    else:
        amount_num = 1
    return amount_num

#RFM Model End 

#Product list Start

def listall(request):
 
    products = Product.objects.all().order_by('-id') #依據id欄位遞減排序顯示所有資料
    return render(request,'watsons/listall.html',locals())


#Product list End









