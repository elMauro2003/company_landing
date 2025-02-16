from django.urls import path
from .views import robots, security, humans, sitemap, handler404, handler500

urlpatterns = [
    # SEO urls
    path('robots.txt', robots, name='robots'),
    path('security.txt', security, name='security'),
    path('humans.txt', humans, name='humans'),
    path('sitemap.txt', sitemap, name='sitemap'),
    path('404/', handler404, name='404'),
    path('500/', handler500, name='500'),
]