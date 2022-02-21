from django.shortcuts import render, get_object_or_404

from cart.cart import Cart, CATEGORY_MAPPING
from .forms import OrderCreateForm
from .models import OrderItem



def order_create(request):
    cart = Cart(request)
    print("erewr", cart)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        print("form", form)
        if form.is_valid():
            order = form.save()
            print("order", order)
            for item in cart:
                print("item_22", item)

                OrderItem.objects.create(order=order,
                                         product=item['category'],
                                         price=item['price']
                                         )
                print("erere",order)
            # очистка корзины
            cart.clear()
            return render(request, 'orders/qiwi.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form})


def qiwi(request):
    return render(request, 'orders/qiwi.html')
