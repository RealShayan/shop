from django.contrib import admin
from .models import City, Product, Inventory, InventoryProduct
from .forms import ProductForm, InventoryProductForm

admin.site.register(City)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_decimal', 'quantity', 'product_image')
    readonly_fields = ('product_image',)
    form = ProductForm

admin.site.register(Product, ProductAdmin)

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')

admin.site.register(Inventory, InventoryAdmin)

class InventoryProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'inventory', 'quantity')
    form = InventoryProductForm

admin.site.register(InventoryProduct, InventoryProductAdmin)





