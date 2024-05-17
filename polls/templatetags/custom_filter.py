from django import template

register = template.Library()

@register.filter
def split(value):
    return value.split('&')

@register.filter
def upper(value):
    return value.upper()