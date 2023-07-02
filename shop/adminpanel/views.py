from django.shortcuts import render
from orders.models import *
from product.models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

class PanelView(UserPassesTestMixin, TemplateView):
    template_name = 'adminpanel.html'
    def test_func(self):
            return self.request.user.is_superuser


#Product

class ProductListView(UserPassesTestMixin, ListView):
    model = Product
    template_name = 'product.html'
    def test_func(self):
            return self.request.user.is_superuser

class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'product_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('product')
    def test_func(self):
            return self.request.user.is_superuser

class ProductDeleteView(UserPassesTestMixin, DeleteView): 
    model = Product 
    template_name = 'product_delete.html' 
    success_url = reverse_lazy('product')
    def test_func(self):
            return self.request.user.is_superuser

#City

class CityListView(UserPassesTestMixin, ListView):
    model = City
    template_name = 'city.html'
    def test_func(self):
            return self.request.user.is_superuser

class CityCreateView(UserPassesTestMixin, CreateView):
    model = City
    template_name = 'city_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('city')
    def test_func(self):
            return self.request.user.is_superuser

class CityDeleteView(UserPassesTestMixin, DeleteView): 
    model = City 
    template_name = 'city_delete.html' 
    success_url = reverse_lazy('city')
    def test_func(self):
            return self.request.user.is_superuser
#Inventory

class InventoryListView(UserPassesTestMixin, ListView):
    model = Inventory
    template_name = 'inventory.html'
    def test_func(self):
            return self.request.user.is_superuser

class InventoryCreateView(UserPassesTestMixin, CreateView):
    model = Inventory
    template_name = 'inventory_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('inventory')
    def test_func(self):
            return self.request.user.is_superuser

class InventoryDeleteView(UserPassesTestMixin, DeleteView): 
    model = Inventory 
    template_name = 'inventory_delete.html' 
    success_url = reverse_lazy('inventory')
    def test_func(self):
            return self.request.user.is_superuser
#InventoryProduct

class InventoryProductListView(UserPassesTestMixin, ListView):
    model = InventoryProduct
    template_name = 'inventoryProduct.html'
    def test_func(self):
            return self.request.user.is_superuser

class InventoryProductCreateView(UserPassesTestMixin, CreateView):
    model = InventoryProduct
    template_name = 'inventoryProduct_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('inventoryProduct')
    def test_func(self):
            return self.request.user.is_superuser

class InventoryProductDeleteView(UserPassesTestMixin, DeleteView): 
    model = InventoryProduct 
    template_name = 'inventoryProduct_delete.html' 
    success_url = reverse_lazy('inventoryProduct')
    def test_func(self):
            return self.request.user.is_superuser
#Order

class OrderListView(UserPassesTestMixin, ListView):
    model = Order
    template_name = 'order.html'
    def test_func(self):
            return self.request.user.is_superuser

class OrderUpdateView(UserPassesTestMixin, UpdateView):
    model = Order
    template_name = 'order_update.html' 
    fields = ['status']
    success_url = reverse_lazy('order')
    def test_func(self):
            return self.request.user.is_superuser

class OrderDeleteView(UserPassesTestMixin, DeleteView): 
    model = Order 
    template_name = 'order_delete.html' 
    success_url = reverse_lazy('order')
    def test_func(self):
            return self.request.user.is_superuser

#---------------------------------------------------------


