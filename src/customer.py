class Customer:
    def __init__(self, input_name, input_wallet, input_age, input_energy_level):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.energy_level = input_energy_level


    def reduce_wallet(self, amount_to_reduce_wallet_by):
        self.wallet -= amount_to_reduce_wallet_by
        
    def check_customer_age(self, customer_age):
        self.age >= customer_age

    def check_caffeine_level(self, amount_caffeine_to_add):
        self.drink.caffeine_level += Customer.energy_level  
