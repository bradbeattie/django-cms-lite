from django.template import Library
from cms_lite.utils import get_cms_pages

register = Library()


@register.assignment_tag
def list_cms_pages(directory=None):
    return get_cms_pages(sub_dirs=[directory] if directory else [])
