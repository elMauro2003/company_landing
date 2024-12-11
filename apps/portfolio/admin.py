from django.contrib import admin
from apps.portfolio.models import Filter, Portfolio, FeaturePortfolio, GalleryPortfolio

# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'get_filter_name', 'description']
    search_fields = ['project_name', 'filter__filter_name']
    list_filter = ('filter',)
    list_per_page = 100

    def get_filter_name(self, obj):
        return obj.filter.filter_name
    get_filter_name.admin_order_field = 'filter'  # Permite ordenar por el campo 'filter'
    get_filter_name.short_description = 'Filter Name'  # Nombre que se mostrará en el encabezado de la columna

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ['filter_slug', 'filter_name']
    search_fields = ['filter_slug', 'filter_name']
    list_per_page = 100

@admin.register(FeaturePortfolio)
class FeaturePortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'portfolio']
    search_fields = ['name', 'portfolio__project_name', 'description']
    list_filter = ('portfolio',)
    list_per_page = 100

@admin.register(GalleryPortfolio)
class GalleryPortfolioAdmin(admin.ModelAdmin):
    list_display = ['name', 'portfolio']
    search_fields = ['name', 'portfolio__project_name']
    list_filter = ('portfolio',)
    list_per_page = 100