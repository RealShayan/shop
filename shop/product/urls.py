from django.urls import path
from .views import Shop

urlpatterns = [
    path('', Shop, name='shop_page'),
]
