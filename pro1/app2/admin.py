from django.contrib import admin
from . models import Cart
from . models import Product
from . models import OrderItem
from . models import Order

# Register your models here.
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)