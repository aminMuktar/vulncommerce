from django.contrib import admin
from .models import Cart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_displays=[
        'cart_id',
        'date_added',
        'quantity',
        'product'
    ]
admin.site.register(Cart)



