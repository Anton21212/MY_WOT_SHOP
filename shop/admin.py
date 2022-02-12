from django.contrib import admin
from .models import Category_Shop, Country, Category_Tanks, Tanks, Fuel

admin.site.register(Category_Shop)
admin.site.register(Country)
admin.site.register(Category_Tanks)
admin.site.register(Tanks)
admin.site.register(Fuel)