from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def nbsp(value):
    if value is not None:
        val = str(value)
        return mark_safe("&nbsp;".join(val.split(' ')))
    else:
        return None
