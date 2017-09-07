from django.db import models

# Create your models here.

class Product(models.Model):
    name =  models.CharField(max_length=255)
    description =  models.TextField(blank=True)
    price =  models.DecimalField(
            max_digits=7,
            default=0,
            decimal_places=2)
    stock =  models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Client(models.Model):
    name =  models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name

class Sale(models.Model):
    destiny = models.CharField(max_length=255, blank=True)
    date_sale = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(blank=True)
    state = models.BooleanField(default=False, verbose_name='activa')
    client = models.ForeignKey(Client)
    product = models.ForeignKey(Product)

    def __str__(self):
        return "%s - %s" % (self.client.name, self.product.name)
