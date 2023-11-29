from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_from_id = Product.objects.get(id= request.POST['id'])
    price_from_form = product_from_id.price
    total_charge = quantity_from_form * price_from_form
    # print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/thanks')

def thanks(request):
    total_ordered=0 ; sum_total_price=0
    for obj in Order.objects.all():
        total_ordered += obj.quantity_ordered
        sum_total_price += obj.total_price
    context = {
        'quantity_ordered' : total_ordered,
        'total_price' : sum_total_price,
    }
    return render(request, 'checkout.html', context)