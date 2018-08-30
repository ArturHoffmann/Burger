from django import forms
from django.forms import ModelForm



from FoodTruck.models import Burger, Toppings, Cash


class BurgerForm(ModelForm):
    class Meta:
        model = Burger
        fields = ['name', 'toppings', 'base_price']


class ToppingsForm(ModelForm):
    class Meta:
        model = Toppings
        fields = ['name', 'price']


class CashForm(ModelForm):
    class Meta:
        model = Cash
        fields = ['name', 'sum_price']





