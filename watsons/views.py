from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse
import json
import numpy as np 
import pandas as pd 

from .models import Transaction, Product, Customer


class IndexView(generic.ListView):
    template_name = 'watsons/index.html'
    context_object_name = 'latest_transaction_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Transaction.objects.order_by('-time')[:5]


class DetailView(generic.DetailView):
    model = Transaction
    template_name = 'watsons/detail.html'



# class RFM_model(TransactionTable):
    





