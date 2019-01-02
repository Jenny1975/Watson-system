from django.contrib import admin
from .models import Customer, Transaction, Bonus, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Bonus)
admin.site.register(Product)