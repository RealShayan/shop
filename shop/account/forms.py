from django import forms
from django.contrib.auth.models import User
from product.models import City

class RegisterForms(forms.Form):
    first_name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام"}))
    last_name = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام خانوادگی"}))
    email = forms.EmailField(required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "ایمیل"}))
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری"}))
    city = forms.ModelChoiceField(queryset=City.objects.all(),required=True,
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "شهر"}))
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("نام کاربری وارد شده موجود می باشد")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("ایمیل وارد شده موجود می باشد")
        return email


class LoginForms(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور"}))