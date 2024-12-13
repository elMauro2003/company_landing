from django.contrib import admin
from apps.general.models import *
from solo.admin import SingletonModelAdmin
# Register your models here.

admin.site.register(Hero,SingletonModelAdmin)
admin.site.register(About,SingletonModelAdmin)
admin.site.register(AltFeatures)

admin.site.register(Pricing)
admin.site.register(Testimonials)
admin.site.register(Team)
admin.site.register(Contact)

@admin.register(ClientContact)
class AdminClientContact(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'phone_number', 'service', 'created_at',]
    search_fields = ['name', 'last_name', 'email', 'phone_number', 'service',]
    list_filter = ('service',)
    list_per_page = 100
    
    
class AdminFAQ(admin.TabularInline):
    model = FAQ
    raw_id_fields = ('service',)
    list_display = ('service',)
    extra = 0

@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display = ['title', 'icon', 'color']
    search_fields = ['title', 'description', 'long_description']
    list_filter = ('color',)
    inlines = [AdminFAQ,]
    list_per_page = 100