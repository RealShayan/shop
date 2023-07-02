from django import forms
from .models import Order
from product.models import *

class OrderCheckForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = []
    def __init__(self, *args, **kwargs):
        global change_order
        change_order = kwargs.get('instance')
        super(OrderCheckForm, self).__init__(*args, **kwargs)

    def clean_product(self):
        user = self.cleaned_data.get('user')
        product = self.cleaned_data.get('product')
        product = Product.objects.get(name__exact=product)
        product_city = product.inp_product.filter(inventory__city__name__exact=user.usercity)
        if not product_city:
            raise forms.ValidationError(f'این محصول در شهر کاربر وجود ندارد')

        return product

    def clean_inventory(self):
        user = self.cleaned_data.get('user')
        product = self.cleaned_data.get('product')
        inventory = self.cleaned_data.get('inventory')
        if product is not None:
            inventoryproduct = InventoryProduct.objects.filter(product__name__exact=product, inventory__name__exact=inventory)
            inventoryuser = Inventory.objects.filter(name__exact=inventory,city__name__exact=user.usercity)
            if not inventoryproduct:
                raise forms.ValidationError(f'این محصول در این انبار وجود ندارد')

            elif not inventoryuser:
                raise forms.ValidationError(f'این انبار مربوط به شهر این کاربر نیست')

        return inventory


    def clean_quantity(self):
        product = self.cleaned_data.get('product')
        quantity = self.cleaned_data.get('quantity')
        inventory = self.cleaned_data.get('inventory')
        last_quantity = None
        if product is not None and inventory is not None:
            product = Product.objects.filter(name__exact=product).first()
            if change_order is None:
                correct_quantity = quantity
            elif change_order is not None:
                order = product.O_product.get(id=change_order.id)
                last_quantity = order.quantity
                correct_quantity = last_quantity - quantity

            product_quantity = product.inp_product.filter(quantity__gte=correct_quantity, inventory=inventory)
            print(product_quantity)
            if not product_quantity:
                raise forms.ValidationError(f'مقدار ثبت شده بیش از موجودی است')
            else:
                used_quantity = quantity if change_order is None else (quantity - order.quantity) if last_quantity < quantity else quantity
                inventoryproduct = InventoryProduct.objects.filter(inventory=inventory, product=product).first()
                if last_quantity is None or last_quantity < quantity:
                    product.quantity -= used_quantity
                    inventoryproduct.quantity -= used_quantity
                else:
                    product.quantity += last_quantity - used_quantity
                    inventoryproduct.quantity += last_quantity - used_quantity
            product.save()
            inventoryproduct.save()

        return quantity

    def clean_status(self):
        status = self.cleaned_data.get('status')
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        inventory = self.cleaned_data.get('inventory')
        last_status = None
        if change_order is not None:
            order = product.O_product.get(id=change_order.id)
            last_status = order.status
        if inventory and product and quantity and last_status != 'cancel':
            product = Product.objects.get(name__exact=product)
            inventoryproduct = InventoryProduct.objects.get(inventory=inventory, product=product)
            if status=='cancel':
                product.quantity += quantity
                inventoryproduct.quantity += quantity
            product.save()
            inventoryproduct.save()
        elif last_status == 'cancel':
            raise forms.ValidationError(f'شما نمیتوانید تنظیمات سفارشات لغو شده را تغییر دهید')

        return status


class OrderForm(forms.Form):
    quantity_need = forms.IntegerField(min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "مقدار مورد نظر خود را وارد کنید"}))
