from pages.models import Page
from django import template

register = template.Library()

@register.simple_tag
def get_pages():
    pages = Page.objects.all()
    return pages