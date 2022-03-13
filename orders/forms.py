from django import forms
from django.forms import ModelForm, TextInput

from orders.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name','address','paid']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-name',
                'placeholder': 'Ваше имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-name',
                'placeholder': 'Ваша фамилия'
            }),
            "address": TextInput(attrs={
                'class': 'form-name',
                'placeholder': 'Ваш город'
            }),
        }


