
class CoffeeShop:
    def __init__(self, input_name, input_till, input_drinks):
        self.name = input_name
        self.till = input_till
        self.drinks = input_drinks

    
    def increase_till(self, amount_to_increase_till_by):
        self.till += amount_to_increase_till_by

    def sell_drink(self, drink_to_sell_to_customer, customer_to_sell_to):
        self.drinks
        # We need "drink_to_sell_to_customer" in order to know what drink to sell. 
        # We need to know it's price
        # We need "customer_to_sell_to" in order to know who to sell to. 
        # Customer has energy and age which we need to check and also a wallet 
        # where we get money to pay for the drink
        if customer_to_sell_to.energy_level > 50:
            return
        # customer wallet decreases by price of drink - done
        # till increases by price of drink - done
        # energy level increases
        # age check (where does the check need to occur?)
        customer_to_sell_to.reduce_wallet(drink_to_sell_to_customer.price)
        self.increase_till(drink_to_sell_to_customer.price)

    # def refuse_if_energy_level_too_high(self, maximum_energy_level):
    #     self.customer.energy_level < maximum_energy_level


