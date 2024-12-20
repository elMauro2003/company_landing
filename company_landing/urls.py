from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.general.urls')),
    path('users/', include('apps.users.urls')),
    path('portfolio/', include('apps.portfolio.urls.portfolio_urls')),
    path('seo/', include('seo.urls')),
    #path('', include('django.contrib.auth.urls')),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
