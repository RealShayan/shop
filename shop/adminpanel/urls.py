from django.urls import path
from .views import *

urlpatterns = [
    path('panel', PanelView.as_view(), name="panel"),

    path('product', ProductListView.as_view(), name="product"),
    path('product/new', ProductCreateView.as_view(), name="product_new"),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),

    path('city', CityListView.as_view(), name="city"),
    path('city/new', CityCreateView.as_view(), name="city_new"),
    path('city/<int:pk>/delete/', CityDeleteView.as_view(), name="city_delete"),

    path('inventory', InventoryListView.as_view(), name="inventory"),
    path('inventory/new', InventoryCreateView.as_view(), name="inventory_new"),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name="inventory_delete"),

    path('inventoryProduct', InventoryProductListView.as_view(), name="inventoryProduct"),
    path('inventoryProduct/new', InventoryProductCreateView.as_view(), name="inventoryProduct_new"),
    path('inventoryProduct/<int:pk>/delete/', InventoryProductDeleteView.as_view(), name="inventoryProduct_delete"),

    path('order', OrderListView.as_view(), name="order"),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name="order_update"),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name="order_delete"),

]
