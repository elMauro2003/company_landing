from django.shortcuts import render

from apps.portfolio.models import Portfolio

# Create your views here.

def portfolio_detail(request,slug):
    project=Portfolio.objects.get(slug=slug)
    
    is_portfolio_detail = request.path.startswith('/portfolio')
    context = {
        'project': project,
        'is_portfolio_detail': is_portfolio_detail,
    }
    
    return render(request, 'landing_page/portfolio/portfolio_detail.html', context)