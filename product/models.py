from django.db import models
from django.utils.safestring import mark_safe

class City(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='نام شهر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر ها'

class Product(models.Model):
    STATUS = (
        ('kg', 'کیلوگرم'),
        ('pack', 'بسته'),
        ('num', 'عدد'),
    )
    name = models.CharField(max_length=120, unique=True, verbose_name='نام')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    quantity = models.PositiveIntegerField(verbose_name='موجودی')
    unit = models.CharField(max_length=20, choices=STATUS, verbose_name='واحد')
    image = models.ImageField(upload_to='product/%Y/%B/%d/', verbose_name='تصویر')

    def __str__(self):
        return self.name

    def price_decimal(self):
        return f'{self.price:,}'
    price_decimal.short_description = 'قیمت'

    def product_image(self):
        return mark_safe('<img src="{}" width="80" style="border-radius:50%;" />'.format(self.image.url))

    product_image.short_description = 'تصویر'
    product_image.allow_tags = True

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class Inventory(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='نام انبار')
    city = models.ForeignKey(City, related_name='inv_city',on_delete=models.CASCADE ,verbose_name='شهر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'انبار'
        verbose_name_plural = 'انبار ها'

class InventoryProduct(models.Model):
    product = models.ForeignKey(Product, related_name='inp_product',on_delete=models.CASCADE ,verbose_name='محصول')
    inventory = models.ForeignKey(Inventory, related_name='inp_inventory', on_delete=models.CASCADE, verbose_name='انبار')
    quantity = models.PositiveIntegerField(verbose_name='موجودی کالا')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'موجودی انبار'
        verbose_name_plural = 'موجودی انبار ها'
        unique_together = [("product", "inventory")]
