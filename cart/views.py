from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Fuel, Tanks
from .cart import Cart

from .forms import CartAddProductForm
CATEGORY_MAPPING = {
    "Fuel": Fuel,
    "Tanks": Tanks
}

def cart_add(request, category, product_id):
    cart = Cart(request)
    category_model = CATEGORY_MAPPING.get(category)

    product = get_object_or_404(category_model, id=product_id)


    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity']
                 )

    return redirect('cart:cart_detail')


def cart_remove(request, category, product_id):
    cart = Cart(request)
    category_model = CATEGORY_MAPPING.get(category)
    product=get_object_or_404(category_model, id=product_id)

    cart.remove(product)
    return redirect('cart:cart_detail')



def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    return render(request, 'cart/detail.html', {'cart': cart})



