from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserCity

class UserCityInline(admin.StackedInline):
    model = UserCity
    verbose_name = 'شهر'

class ExtendUserAdmin(UserAdmin):
    inlines = (UserCityInline, )

admin.site.unregister(User)
admin.site.register(User, ExtendUserAdmin)
