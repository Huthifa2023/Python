import store,product

ramallah = store.Store('Ramallah')
nablus = store.Store('Nablus')

egg = product.Product('Egg', 1, 'food')
bread = product.Product('Bread', 3, 'food')
milk = product.Product('Milk', 10, 'food')
soap = product.Product('Soap', 5, 'cleaning')
shampoo = product.Product('Shampoo', 18, 'cleaning')
heater = product.Product('Heater', 160, 'tools')
speaker = product.Product('Speaker', 35, 'tools')

ramallah.add_product(egg).add_product(bread).add_product(milk).add_product(shampoo).add_product(heater).add_product(speaker)
nablus.add_product(egg).add_product(bread).add_product(milk).add_product(soap).add_product(heater).add_product(speaker)

# Tests belwo:

nablus.print_available_products_with_prices()
nablus.set_clearance('food', 0.5)
print('prices after liberation')
nablus.print_available_products_with_prices()

# nablus.print_available_products_with_prices()
# nablus.inflation(.9)
# print('pricses after inflation')
# nablus.print_available_products_with_prices()

# ramallah.print_available_products_with_prices()

# egg.update_price(0.02, True).print_info()
# heater.update_price(0.1, True).print_info()
# milk.update_price(0.05, False).print_info()

