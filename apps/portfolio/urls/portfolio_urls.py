from django.urls import path

from apps.portfolio.views.portfolio_views import portfolio_detail



urlpatterns = [
    path('<slug:slug>/', portfolio_detail, name='portfolio_detail'),
] 
