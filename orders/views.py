from django.shortcuts import render, get_object_or_404

from cart.cart import Cart

from orders.forms import OrderForm
from orders.models import OrderItem

from shop.models import Fuel, Tanks

CATEGORY_MAPPING = {
    "Fuel": Fuel,
    "Tanks": Tanks
}

def order(request):
    cart = Cart(request)
    error = ''
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product_tanks=item['title'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            form.save()
            return render(request, 'orders/payment.html', {'order': order})
        else:
            error = 'Форма не верно заполнена'

    form = OrderForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'orders/order.html', data)


def payment(request):
    return render(request, 'orders/payment.html')
