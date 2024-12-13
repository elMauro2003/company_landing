from django.urls import path
from . import views
from apps.general.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('create-contact/', create_contact, name='create_contact'),
    path('client-contact/', client_contact, name='client_contact'),
    path('service-detail/<int:pk>/', service_detail, name='serivce_detail'),
    path('get_started/', get_started, name='get_started'),
    
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)