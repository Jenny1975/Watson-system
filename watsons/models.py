from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    gender = models.IntegerField
    birthday = models.DateTimeField


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.IntegerField
    price = models.IntegerField
    brand = models.IntegerField  # could be a foreignkey ?
    quantity = models.IntegerField


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField('date published')
    amount = models.IntegerField

class Location(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Bonus(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate = models.FloatField
    period = models.DateTimeField
