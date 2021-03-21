from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) #a user can only have one customer and customer can only have one user
    name = models.CharField(max_length = 100, null= True)
    email = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length= 200, null= True)
    price = models.FloatField()
    #product =
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null=True, blank=True)
    date_ordered= models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default= False)
    transaction_id= models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):             #The Cart
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.CharField(max_length= 100, null=False)
    address= models.CharField(max_length= 100, null=False)
    city = models.CharField(max_length= 100, null=False)
    state = models.CharField(max_length= 100, null=False)
    zipcpode = models.CharField(max_length= 100, null=False)
    date_added = models.CharField(max_length= 100, null=True)

    def __str__(self):
        return self.address
