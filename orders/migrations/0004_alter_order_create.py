# Generated by Django 4.2.2 on 2023-07-02 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_create_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت سفارش'),
        ),
    ]
