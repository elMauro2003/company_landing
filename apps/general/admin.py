from django.contrib import admin
from apps.general.models import *
from solo.admin import SingletonModelAdmin
# Register your models here.

admin.site.register(Hero,SingletonModelAdmin)

admin.site.register(AltFeatures)

admin.site.register(Pricing)
admin.site.register(Testimonials)
admin.site.register(Team)
admin.site.register(Contact)

admin.site.register(PricingSection, SingletonModelAdmin)
admin.site.register(TestimonialSection, SingletonModelAdmin)
admin.site.register(TeamSection, SingletonModelAdmin)
admin.site.register(ContactSection, SingletonModelAdmin)
admin.site.register(ServiceSection, SingletonModelAdmin)
admin.site.register(PortfolioSection, SingletonModelAdmin)
admin.site.register(FAQSection, SingletonModelAdmin)


@admin.register(ClientContact)
class AdminClientContact(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'service', 'created_at',]
    search_fields = ['first_name', 'last_name', 'email', 'phone_number', 'service',]
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
    
    
class TermPoint(admin.TabularInline):
    model = TermPoint
    raw_id_fields = ('term',)
    list_display = ('term',)
    extra = 0

@admin.register(Term)
class AdminTerm(SingletonModelAdmin):
    list_display = ['pk']
    inlines = [TermPoint,]


class TextAboutPoint(admin.TabularInline):
    model = TextAbout
    raw_id_fields = ('about',)
    list_display = ('about',)
    extra = 0

@admin.register(About)
class AdminAbout(SingletonModelAdmin):
    list_display = ['pk','title','subtitle']
    inlines = [TextAboutPoint,]