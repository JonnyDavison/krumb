from django.contrib import admin
from .models import Product, Category, Gallery

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ Organise the Products admin panel """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'tag',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """ Organise the Category admin panel """
    list_display = (
        'friendly_name',
        'name',
    )
    

class GalleryAdmin(admin.ModelAdmin):
    """ Organise the Gallery admin panel """
    list_display = (
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)