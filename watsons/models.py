from django.db import models




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
    birthday = models.DateTimeField(blank=True, null=True)

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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)
    amount = models.IntegerField()
    def total(self):
        amount = self.amount
        product = self.product
        total_amount = amount*product.price
        return total_amount


class Location(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=10)

    def __str__(self):
        return self.location_name

class Bonus(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5, decimal_places=2, default = 0)
    period = models.DateTimeField(blank=True, null=True)


# below are all new class
#

class Pocket_other(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_Cosmetic = models.IntegerField(default=0)
    total_Snacks = models.IntegerField(default=0)
    total_Care = models.IntegerField(default=0)



class Servive(models.Model):
    Num = models.IntegerField(default=0)
    Date = models.IntegerField(default=0)
    retentention_rate = 0
    servive_rate = 0
    respected_customer_num = 0
    customer_num = 0
    def count(self,r,s):
        self.retentention_rate = r
        self.servive_rate = self.retentention_rate * s
        self.customer_num = 100*self.servive_rate
        self.respected_customer_num = self.customer_num*self.Date








