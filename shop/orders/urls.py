from django.urls import path
from .views import OrderSubmit, OrdersList

urlpatterns = [
    path('order/<int:inventoryid>/', OrderSubmit, name='submit_order'),
    path('orders_list/<int:user_id>/', OrdersList, name='order_list'),
]