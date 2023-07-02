from django.contrib import admin
from .models import Order
from .forms import OrderCheckForm

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user' ,'product' ,'inventory', 'quantity', 'status')
    form = OrderCheckForm

admin.site.register(Order, OrderAdmin)
