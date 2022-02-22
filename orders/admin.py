from django.contrib import admin

# Register your models here.
from .models import Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields=['product']

class OrderAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'first_name',
        'last_name',
        'email',
        'ip_address',
        'city',
        'created_at',
        'updated_at',
        'status',
    ]
    list_filter=[
        'created_at',
        'updated_at',
        'status',
    ]
    inlines=[OrderItemInline]

admin.site.register(Order,OrderAdmin)

