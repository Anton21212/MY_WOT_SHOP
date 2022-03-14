"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import shop
from main import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('main_page2', views.main_page2, name='main_page2'),
    path('autorization/', views.user_login, name='autorization'),
    path('registration/', views.register, name='registration'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('profile/', views.profile, name='profile'),

    # Подключение шопа категории
    path('category_shop/', include('shop.urls')),

    # Подключение корзины
    path('cart/', include('cart.urls')),

    # Подключение покупок
    path('orders/', include('orders.urls')),

    #подключение саппорта
    path('api/v1/tikets/', include('support.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
