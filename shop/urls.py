from django.urls import path

from . import views

app_name = 'category_shop'

urlpatterns = [
    # Подключение шопа категории

    path('', views.shop_category, name='shop'),

    path('fuel/', views.all_fuels, name='fuel'),

    path('country/', views.country_all, name='country'),

    path('<country>/tanks', views.country_tanks, name='country_tanks'),

]
