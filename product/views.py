from django.shortcuts import render, redirect
from .models import Product, InventoryProduct
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Shop(request):
    if request.user.is_authenticated:
        user = request.user
        products = InventoryProduct.objects.filter(inventory__city=user.usercity.city)
    else:
        products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(request, 'product/shop.html', context)