from django.shortcuts import render
from django.http import HttpResponse
from .model import Transaction

# Create your views here.
def index(request):
    latest_transaction_list = Transaction.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_transaction_list': latest_transaction_list,
    }
    return HttpResponse(template.render(context, request))