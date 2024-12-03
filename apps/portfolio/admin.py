from django.contrib import admin

from apps.portfolio.models import Filter, Portfolio

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Filter)