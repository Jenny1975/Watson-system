from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    login_date = models.DateTimeField('date published')


class Product(models.Model):
    product_name = models.CharField(max_length=30)


class Order(models.Model):
    check_date = models.DateTimeField('date published')