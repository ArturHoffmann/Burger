# from django.core.serializers import json
import json

import jsonpickle
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views import View

from FoodTruck.forms import BurgerForm, ToppingsForm, CashForm
from FoodTruck.model.BurgerUtils import BurgerUtils
from FoodTruck.model.Order import Order
from FoodTruck.model.OrderItem import OrderItem
from FoodTruck.models import Burger, Toppings


class BurgerView(View):
    def get(self, request):
        form = BurgerForm()
        if request.GET.get('r') is not None:
            try:
                del request.session['order']
            except KeyError:
                pass
        return render(request, 'menu.html', {"form": form, "burgers": Burger.objects.all()})


class ToppingsView(View):
    def get(self, request):
        form = ToppingsForm()
        return render(request, 'toppings.html', {"form": form,
                                                 "toppings": Toppings.objects.all()})

    def post(self, request):
        order = Order()
        order_serialized = request.session.get('order')

        if order_serialized:
            order = jsonpickle.loads(order_serialized)

        burger_name = request.POST['burger_name']
        burger = Burger.objects.get(name=burger_name)

        topping_data = BurgerUtils.get_topping_data(burger)

        order.add_item(OrderItem(burger, []))
        request.session['order'] = jsonpickle.dumps(order)

        return render(request, 'toppings.html', {'topping_data': topping_data,
                                                 'burger': burger,
                                                 'order_item_id': len(order.get_items()) - 1})


class CashView(View):
    def post(self, request):
        order_serialized = request.session.get('order')
        if not order_serialized:
            HttpResponse("brak zamówienia")

        order = jsonpickle.loads(order_serialized)

        item_id = request.POST['order_item_id']
        this_item = order.get_items()[int(item_id)]
        this_item.toppings = BurgerUtils.get_post_topping_data(this_item.burger, request.POST)
        request.session['order'] = jsonpickle.dumps(order)

        if request.POST['option'] == 'MENU':
            return redirect('/burger')

        order.calculate_price()

        return render(request, 'cash.html', {'order': order})
