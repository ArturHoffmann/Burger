from FoodTruck.models import Toppings


class Order:
    def __init__(self):
        self.__items = []
        self.price = 0.0

    def get_items(self):
        return self.__items

    def add_item(self, order_item):
        self.__items.append(order_item)

    def calculate_price(self):
        self.price = 0.0
        for e in self.__items:
            price_of_this_burger = e.burger.base_price
            all_additions_price = 0
            for additional in e.toppings:
                amount = additional['amount']
                additional_name = additional['name']
                this_addition_price = amount * Toppings.objects.get(name=additional_name).price
                all_additions_price += this_addition_price
            price_of_this_burger += all_additions_price
            self.price += float(price_of_this_burger)

