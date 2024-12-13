from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)


#create an OrderItem inline

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

#extend our Order Model

class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ['date_ordered']
    #fields = ['user', 'full_name']
    inlines = [OrderItemInline]

#unregister order model

admin.site.unregister(Order)

#re register Order and OrderItems

admin.site.register(Order, OrderAdmin)