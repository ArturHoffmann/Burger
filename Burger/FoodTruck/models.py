from django.db import models

# Create your models here.



class Toppings(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)


class Burger(models.Model):
    name = models.CharField(max_length=255)
    toppings = models.ManyToManyField(Toppings)
    base_price = models.DecimalField(max_digits=4, decimal_places=2)


class Cash(models.Model):
    name = models.CharField(max_length=512)
    sum_price = models.DecimalField(max_digits=6, decimal_places=2)




