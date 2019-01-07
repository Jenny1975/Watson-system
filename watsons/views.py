from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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


def RFM_model(request):
    transaction_list = Transaction.objects.order_by('delta_date')
    customer_list = Customer.objects.all()

    # customer_1 = []
    # customer_2 = []
    # customer_3 = []
    # customer_4 = []
    # customer_5 = []
    # customer_6 = []
    # customer_7 = []
    # customer_8 = []

    # for transaction in transaction_list:
    #     if transaction.customer_id == 1:
    #         customer_1.append(transaction)
    #     elif transaction.customer_id == 2:
    #         customer_2.append(transaction)
    #     elif transaction.customer_id == 3 :
    #         customer_3.append(transaction)
    #     elif transaction.customer_id == 4:
    #         customer_4.append(transaction)
    #     elif transaction.customer_id == 5:
    #         customer_5.append(transaction)
    #     elif transaction.customer_id == 6:
    #         customer_6.append(transaction)
    #     elif transaction.customer_id == 7:
    #         customer_7.append(transaction)
    #     else:
    #         customer_8.append(transaction)
    
    # customer_transaction_list = [customer_1, customer_2, customer_3, customer_4, customer_5, customer_6, customer_7, customer_8]

    customer_transaction_list = []
    for cm in customer_list:
        customertransaction_list = cm.transaction_set.order_by('delta_date')
        customer_transaction_list.append(customertransaction_list)
    
    for customer_t in customer_transaction_list:
        customer_t.recent_num = create_recent_number(customer_t)
        # customer_t.append(create_average_spending(customer_t))
    
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
    
    for customer in customer_transaction_list:
        if customer.recent_num == 5:
            count_5 += 1
            total_5 += customer[0].transaction_total
        elif customer.recent_num == 4:
            count_4 += 1
            total_4 += customer[0].transaction_total
        elif customer.recent_num == 3:
            count_3 += 1
            total_3 += customer[0].transaction_total
        elif customer.recent_num == 2:
            count_2 += 1
            total_2 += customer[0].transaction_total
        else:
            count_1 += 1
            total_1 += customer[0].transaction_total
    
    average_5 = total_5 / count_5
    average_4 = total_4 / count_4
    average_3 = total_3 / count_3
    average_2 = total_2 / count_2
    average_1 = total_1 / count_1
    
    dataset = [{'recent': 5, 'average_amount': average_5},
                {'recent': 4, 'average_amount': average_4},
                {'recent': 3, 'average_amount': average_3},
                {'recent': 2, 'average_amount': average_2},
                {'recent': 1, 'average_amount': average_1},]


    return render(request, 'watsons/detail.html', {'dataset': dataset})

def create_recent_number(list):
    customer_recent_transaction = list [0]
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
    customer_recent_transaction = list [-1]
    first_day = customer_recent_transaction.delta_date
    count = 0
    for i in list:
        count += 1
    frquency = recent_day / count
    if frquency < 8:
        frquency_num = 5
    elif frquency_day < 15:
        frquency_num = 4
    elif frquency_day < 22:
        frquency_num = 3
    elif frquency_day < 29:
        frquency_num = 2
    else:
        frquency_num = 1
    return frquency_num

# def create_average_spending(list):
#     customer_transaction = list
#     count = 0
#     total = 0
#     for transaction in customer_transaction:
#         total += transaction.transaction_total
#         count += 1
#     average = total / count
#     return average 











