from django.contrib import admin
from .models import  Country, Category_Tanks, Tanks, Fuel

admin.site.register(Country)
admin.site.register(Category_Tanks)
admin.site.register(Tanks)
admin.site.register(Fuel)
