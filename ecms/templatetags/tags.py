from mezzanine import template

register = template.Library()

@register.simple_tag
def display(val):
    return ""
