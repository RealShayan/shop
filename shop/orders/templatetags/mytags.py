from django import template
register = template.Library()

@register.simple_tag
def multiply(price, quantity, *args, **kwargs):
    Price = int(price) * int(quantity)
    return f'{Price:,}'

@register.simple_tag
def decimal_price(price, *args, **kwargs):
    return f'{price:,}'