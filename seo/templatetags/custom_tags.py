from django.conf import settings
from django.urls import reverse
from django import template
#from app.public.models import CaseStudyListPage, BlogListPage

register = template.Library()


@register.simple_tag
def url_absolute(page):
    return settings.DOMAIN_URL + reverse(page)
