from django.contrib import admin
from apps.general.models import *
from solo.admin import SingletonModelAdmin
# Register your models here.

admin.site.register(Hero,SingletonModelAdmin)
admin.site.register(About,SingletonModelAdmin)
admin.site.register(AltFeatures)
admin.site.register(Services)
admin.site.register(FAQ)
admin.site.register(Pricing)
admin.site.register(Testimonials)
admin.site.register(Team)
admin.site.register(Contact)

