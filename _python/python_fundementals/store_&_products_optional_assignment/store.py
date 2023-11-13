class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        del self.products[id]
        return self

    def inflation(self, percent_increase):
        for i in self.products:
            i.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for j in self.products:
            if j.category == category:
                j.update_price(percent_discount, False)
        return self
    def print_available_products_with_prices(self):
        for i in self.products:
            print(i.name,'@',i.price,'\n')
        return self