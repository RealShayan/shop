from django.urls import path
from .views import login_view, register_view, logout_view

urlpatterns = [
    path('login/', login_view, name='user_login'),
    path('register/', register_view, name='user_register'),
    path('logout/', logout_view, name='user_logout'),
]