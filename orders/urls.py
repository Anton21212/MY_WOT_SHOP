from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order'),
    path('payment', views.payment, name='payment')
]
