from django import template

register = template.Library()

@register.filter
def upto(num, x):
    return range(num, x)