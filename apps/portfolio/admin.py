from django.contrib import admin

from apps.portfolio.models import *

# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['project_name','filter']
    search_fields = ['project_name','filter']
    list_filter = (
        'filter',
    )
    list_per_page = 100

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ['filter','filter_name']
    search_fields = ['filter','filter_name']
    list_per_page = 100

@admin.register(FeaturePortfolio)
class FeaturePortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','icon','portfolio']
    search_fields = ['name','portfolio','description']
    list_filter = (
        'portfolio',
    )
    list_per_page = 100

@admin.register(GalleryPortfolio)
class GalleryPortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','portfolio']
    search_fields = ['name','portfolio']
    list_filter = (
        'portfolio',
    )
    list_per_page = 100
