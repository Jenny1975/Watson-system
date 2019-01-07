from django.shortcuts import get_object_or_404, render, get_list_or_404,\
     redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.urls import reverse
from django.db import models
from decimal import Decimal
from .models import Transaction, Product, Customer
from django.db.models import Avg, Sum

import csv
import random
import datetime

# for the datetime is hard to create in the required form
# all the datetime information is given in the create function
# except for birthday, which may not be used temporily
NOW =  datetime.datetime.now()

# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")


# this function regardless of redundant 
# don't call this function twice
def create(request):
    with open('Pfile.csv') as pf:
        first = True
        data = csv.reader(pf, delimiter=',')
        for each in data:
            if first:
                first =False
                pass
            else:
                c, created = Product.objects.get_or_create(product_name=each[0], 
                                                        category=each[1],
                                                        price=int(each[2]),
                                                        quantity=int(each[3]))
                if not created:
                    c.save()

    with open('Cfile.csv') as cf:
        first = True
        data = csv.reader(cf, delimiter=',')
        for each in data:
            if first:
                first =False
                pass
            else:
                c, created = Customer.objects.get_or_create(customer_name=each[0],
                                                            gender=each[1])
                if not created:
                    c.save()

    with open('Tfile.csv') as tf:
        first = True
        data = csv.reader(tf, delimiter=',')
        for each in data:
            if first:
                first =False
                pass
            else:
                d = random.randint(1,364)
                thisTime = NOW + datetime.timedelta(days=d)
                c, created = Transaction.objects.get_or_create(customer_id=each[0],
                                                            product_id=each[1],
                                                            time=thisTime,
                                                            amount=each[2])
        if not created:
            c.save()
    return HttpResponse('You can')

           

def showTransaction(request):
    allList = Transaction.objects.all()
    yList = Transaction.objects.filter(time__year=2018)
    m1 = Transaction.objects.filter(time__year=2018, time__month=1)
    m2 = Transaction.objects.filter(time__year=2018, time__month=2)
    m3 = Transaction.objects.filter(time__year=2018, time__month=3)
    m4 = Transaction.objects.filter(time__year=2018, time__month=4)
    m5 = Transaction.objects.filter(time__year=2018, time__month=5)
    m6 = Transaction.objects.filter(time__year=2018, time__month=6)
    m7 = Transaction.objects.filter(time__year=2018, time__month=7)
    m8 = Transaction.objects.filter(time__year=2018, time__month=8)
    m9 = Transaction.objects.filter(time__year=2018, time__month=9)
    m10 = Transaction.objects.filter(time__year=2018, time__month=10)
    m11 = Transaction.objects.filter(time__year=2018, time__month=11)
    m12 = Transaction.objects.filter(time__year=2018, time__month=12)

    return render(request, 'watsons/ShowTransaction.html', {'allList': allList})


