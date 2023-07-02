from django import forms
from .models import Product, InventoryProduct
from django.db.models import Sum

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        global change_product
        change_product = kwargs.get('instance')
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['name']
        if change_product:
            product = Product.objects.filter(name__exact=product).first()
            inventories_quantity = product.inp_product.all().aggregate(Sum('quantity'))['quantity__sum']
            if quantity < inventories_quantity:
                raise forms.ValidationError(f'با توجه به موجودی انبارها، اجازه ندارید موجودی را کمتر از {inventories_quantity} تنظیم کنید')
        return quantity

    class Meta:
        model = Product
        exclude = []

class InventoryProductForm(forms.ModelForm):

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product = self.cleaned_data['product']
        inventory = self.cleaned_data['inventory']
        total_quantity = Product.objects.get(id=product.id).quantity
        used_quantity = InventoryProduct.objects.filter(product=product).exclude(inventory=inventory).aggregate(Sum('quantity'))['quantity__sum']
        if used_quantity:
            request_quantity = used_quantity + quantity
        else:
            request_quantity = quantity
        if total_quantity < request_quantity:
            raise forms.ValidationError(f'مقدار درخواستی شما از موجودی کل به تعداد {request_quantity - total_quantity } واحد بیشتر است')
        return quantity

    class Meta:
        model = InventoryProduct
        exclude = []