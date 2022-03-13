

from django.contrib import admin
from .models import Order, OrderItem


# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     raw_id_fields = ['product_tanks']
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'address', 'paid']
#
#     list_filter = ['paid']
#     inlines = [OrderItemInline]
#
#
admin.site.register(Order)
admin.site.register(OrderItem)
