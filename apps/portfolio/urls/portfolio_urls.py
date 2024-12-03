from django.urls import path

from apps.portfolio.views.portfolio_views import portfolio_detail



urlpatterns = [
    path('<int:pk>/', portfolio_detail, name='portfolio_detail'),
] 
