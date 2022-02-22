from django.contrib import admin
from .models import Category,Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name',
                    'slug',
                    'brand',
                    'sku',
                    'price',
                    'old_price',
                    'is_active',
                    'quantity',
                    'description',
                    'created_at',
                    'updated_at',
                    'image',
                    'thumbnail'
                    ]
    list_filter=['is_active','created_at','updated_at']
    list_editable=['price','is_active']
    prepopulated_fields={'slug':('name',)}

admin.site.register(Product,ProductAdmin)



