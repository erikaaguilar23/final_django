from django.db import models
import datetime

# Categories of Products
class Category(models.model):
        name = models.CharField(max_Length=50)

        def __str__(self):
            return self.name
        
# Customers
class Customer(models.model):
      first_name = models.CharField(max_Length=50)
      last_name = models.CharField(max_Length=50)
      phone = models.CharField(max_Length=10)
      email = models.CharField(max_Length=100)
      password = models.CharField(max_Length=100)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'




class Product(models.Model):
    name = models.CharField(max_Lenght=100)
    price = models.CharField(default=0, decimal_places=2, max_digits=6)
    Category = models.Foreignkey(Category, on_delete=models.CASCADE)
    description =models.IntegerField(default=1)
    image = models.CharField(max_Length=100, default=, blank=True)

    def __str__(self):
        return self.name


        
class Order (models.Model):
    product = models.Foreignkey(Product, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=modelsCASCADE)
    quatity = models.IntegerField(default=1)
    address = models.CharField(max_Lenght=100, default=, blank=True)
    phone = models.DateField(default=datetime.datetime.today)
    date = models.DateField(default-datetime.today)
    status = models.BooleanField(default=False)

     def __str__(self):
        return self.product
