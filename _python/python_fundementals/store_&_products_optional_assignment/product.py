class Product:
    def __init__(self, name, price, category,id=0):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            self.price += self.price * percent_change
        elif is_increased is False:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        print(f'product name is {self.name}, within the {self.category} category, with price of {self.price}$')
        return self