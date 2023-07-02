from django.db import models
from product.models import Product, Inventory
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS = (
        ('pending', 'در انتظار بازبینی'),
        ('deliver', 'آماده ارسال'),
        ('Post', 'ارسال شده'),
        ('cancel', 'لغو شده'),
    )
    user = models.ForeignKey(User, related_name='O_user',on_delete=models.CASCADE ,verbose_name='کاربر')
    product = models.ForeignKey(Product, related_name='O_product',on_delete=models.CASCADE ,verbose_name='محصول')
    price = models.PositiveBigIntegerField(verbose_name='قیمت کالا')
    inventory = models.ForeignKey(Inventory, related_name='O_inventory', on_delete=models.CASCADE, verbose_name='انبار')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    status = models.CharField(max_length=15, choices=STATUS, verbose_name='وضعیت سفارش')
    create = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت سفارش')

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
