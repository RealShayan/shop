from django.shortcuts import render, redirect
from product.models import Product, InventoryProduct
from .models import Order
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.contrib import messages


@login_required(login_url='/login')
def OrderSubmit(request,inventoryid):
    inventory = InventoryProduct.objects.get(id__exact=inventoryid)
    order_form = OrderForm(request.POST or None)
    if request.method == 'POST':
        if order_form.is_valid():
            quantity_need = order_form.cleaned_data.get("quantity_need")
            if quantity_need > inventory.quantity:
                order_form.add_error('quantity_need', 'درخواست شما بیشتر از حد مجاز است')
            else:
                Order.objects.create(user=request.user, product=inventory.product, price=inventory.product.price ,inventory=inventory.inventory, quantity=quantity_need, status='pending')
                inventory.quantity -= quantity_need
                inventory.save()
                product = Product.objects.get(id=inventory.product.id)
                product.quantity -= quantity_need
                product.save()
                messages.success(request, 'سفارش شما ثبت شد و در حال پردازش میباشد.')
                return redirect('/')
    context ={
        "inventory" : inventory,
        "order_form": order_form
    }
    return render(request, 'orders/order.html', context)

@login_required(login_url='/login')
def OrdersList(request,user_id):
    orders = Order.objects.filter(user_id__exact=user_id)
    context ={
        "orders" : orders,
    }
    return render(request, 'orders/orders_list.html', context)
