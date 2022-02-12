from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category_Shop, Country, Tanks, Fuel


# Отвечает за вывод всего магазина

def shop_category(request):
    category_all_shop = Category_Shop.objects.all()
    print(category_all_shop)
    return render(request, 'shop/Category_shop.html', {'category_all_shop': category_all_shop})


# Вывод всех стран

def country_all(request):
    country = Country.objects.all()

    return render(request, 'shop/Country.html', {'country': country})



# вывод танков для каждой страны



def country_tanks (request,country):

    tanks = Tanks.objects.filter(country__title__icontains=country)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/Belarus_tanks.html', {'tanks': tanks,
                                                       'cart_product_form':cart_product_form})



# Вывод топлива

def all_fuels(request):

    fuels = Fuel.objects.all()

    return render(request, 'shop/Fuel.html', {'fuels':fuels})




# Может когда-то использую



# def country_tanks_Bel(request,id):
#     context = {}
#     context["Belarus"] = Tanks.objects.get(id=id)
#
#     return render(request, 'shop/Belarus_tanks.html', context)

# def country_tanks_Bel(request):
#
#     tanks = Tanks.objects.filter(country__title__icontains="Беларусь")
#
#     return render(request, 'shop/Belarus_tanks.html', {'tanks': tanks})