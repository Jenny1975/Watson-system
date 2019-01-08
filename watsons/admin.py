from django.contrib import admin
from .models import Customer, Transaction, Bonus, Product, Location, Pocket_other,Servive

# Register your models here.
admin.site.register(Customer)
admin.site.register(Transaction)
admin.site.register(Bonus)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Pocket_other)
admin.site.register(Servive)