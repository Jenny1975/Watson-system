from django.db import models
import time
import datetime



# Create your models here.

class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    gender_choice = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    customer_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices = gender_choice, default = MALE)
    birthday = models.DateField(blank=True, null=True)
    marketing_spending = models.PositiveIntegerField()
    recent_num = 0
    def __str__(self):
        return self.customer_name


class Product(models.Model):
    COSMETIC = 'CO'
    SNACK = 'SA'
    CARE_PRODUCT = 'CR'
    category_choice = (
        (COSMETIC, 'Cosmetic'),
        (SNACK, 'Snacks'),
        (CARE_PRODUCT, 'Care Product'),
    )
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length = 2, choices = category_choice, default = COSMETIC )
    price = models.PositiveIntegerField()
    brand = models.IntegerField  # could be a foreignkey ?
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_name


class Transaction(models.Model):
    transaction_total = models.IntegerField(blank=True, null=True)
    transaction_id = models.PositiveIntegerField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateField(blank=True, null=True)
    delta_date = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField()

    @staticmethod
    def create_total(self):
        product_amount = self.amount
        product = self.product
        # select_product = Product.objects.filter(id = product)
        total_amount = product_amount*product.price
        return total_amount

    
    # def create_transaction_num(self):
    #     num = 0
    #     last_transaction = Transaction.objects.all[-1]
    #     time = self.time
    #     if time == last_transaction.time:
    #         num = last_transaction.num
    #     else:
    #         num = num +1
    #     return num

    def time_delta(self):
        date_now = datetime.date.today()
        delta = date_now - self.time
        return delta.days

    def save(self):
        if self.transaction_total is None:
            self.transaction_total = Transaction.create_total(self)
        # if self.transaction_id is None:
        #     self.transaction_id = self.create_transaction_num(self)
        if self.delta_date is None:
            self.delta_date = Transaction.time_delta(self)
        super().save()



class Location(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=10)

    def __str__(self):
        return self.location_name

class Bonus(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    period = models.DateTimeField(blank=True, null=True)

class Pocket_other(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_other = models.IntegerField(default = 0)




