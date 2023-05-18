from django import template

register = template.Library()

@register.filter
def star_range(value):
    return range(value)