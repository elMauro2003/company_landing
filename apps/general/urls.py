from django.urls import path
from . import views
from apps.general.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('create-contact/', create_contact, name='create_contact'),
    #path('admin/hero/', views.hero_list, name='hero_list'),
    #path('admin/hero/<int:pk>/edit/', views.hero_edit, name='hero_edit'),
    #path('admin/about/', views.about_list, name='about_list'),
    #path('admin/about/<int:pk>/edit/', views.about_edit, name='about_edit'),
    #ath('admin/alt_features/', views.alt_features_list, name='alt_features_list'),
    #path('admin/alt_features/<int:pk>/edit/', views.alt_features_edit, name='alt_features_edit'),
    # Repite lo mismo para las otras secciones
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)