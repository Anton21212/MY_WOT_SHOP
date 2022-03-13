from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from .models import  Country, Tanks, Fuel
from shop.forms import SearchForm

# Отвечает за вывод всего магазина

def shop_category(request):


    return render(request, 'shop/Category_shop.html')



# Вывод всех стран

def country_all(request):
    country = Country.objects.all()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = Tanks.objects.filter(title__icontains=cd['query'])
            total_results = results.count()
        return render(request, 'shop/info.html', {
            'form': form,
            'cd': cd,
            'results': results,
            'total_results': total_results})
    else:
        form = SearchForm()
    return render(request, 'shop/Country.html', {
        'country': country,
        'form': form})


# вывод танков для каждой страны


def country_tanks(request, country):
    tanks = Tanks.objects.filter(country__title__icontains=country)
    cart_product_form = CartAddProductForm()
    category = str(tanks.model._meta.object_name)
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = Tanks.objects.filter(title__icontains=cd['query'])
            total_results = results.count()
        return render(request, 'shop/info.html', {
            'form': form,
            'cd': cd,
            'results': results,
            'total_results': total_results})
    else:
        form = SearchForm()
    return render(request, 'shop/Belarus_tanks.html', {'tanks': tanks,
                                                       'cart_product_form': cart_product_form,
                                                       'category': category,
                                                       'form':form})


# Вывод топлива

def all_fuels(request):
    fuels = Fuel.objects.all()
    cart_product_form = CartAddProductForm()
    category = str(fuels.model._meta.object_name)
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = Fuel.objects.filter(title__icontains=cd['query'])
            total_results = results.count()
        return render(request, 'shop/info.html', {
            'form': form,
            'cd': cd,
            'results': results,
            'total_results': total_results})
    else:
        form = SearchForm()
    return render(request, 'shop/Fuel.html', {
        'fuels': fuels,
        'cart_product_form': cart_product_form,
        'category': category,
        'form': form
        })


def number(request):
    fuels = Fuel.objects.all()
    return render(request,'shop/info.html',{
        'fuels':fuels
    })





