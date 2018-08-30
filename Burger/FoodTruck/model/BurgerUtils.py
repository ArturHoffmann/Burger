from FoodTruck.models import Toppings


class BurgerUtils:
    @staticmethod
    def get_topping_data(burger):
        toppings_in_this_burger = list(burger.toppings.all().values_list("name", flat=True))
        toppings = Toppings.objects.all()
        topping_data = []
        for topping in toppings:
            amount = 0
            if topping.name in toppings_in_this_burger:
                amount = 1
            data = {"name": topping.name,
                    "amount": amount}
            topping_data.append(data)

        return topping_data

    @staticmethod
    def get_post_topping_data(burger, post_data):
        toppings_in_this_burger = list(burger.toppings.all().values_list("name", flat=True))
        post_toppings = [x[4:] for x in post_data if x.startswith('top_')]

        topping_data = []
        for topping_name in post_toppings:
            amount = int(post_data['top_'+topping_name])
            if topping_name in toppings_in_this_burger:
                amount -= 1

            if amount > 0:
                data = {"name": topping_name,
                        "amount": amount,
                        "price": amount * Toppings.objects.get(name=topping_name).price}
                topping_data.append(data)

        return topping_data
