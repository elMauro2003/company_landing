from django.urls import path
from apps.general.views import *


urlpatterns = [
    path('', home, name='home'),
]