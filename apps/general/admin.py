from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.general.models import *

# Register your models here.

admin.site.register(Hero)
admin.site.register(About)
admin.site.register(AltFeatures)
admin.site.register(Services)
admin.site.register(Pricing)
admin.site.register(Portfolio)
admin.site.register(Testimonials)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Filter)
