from django.shortcuts import render

from apps.portfolio.models import Portfolio

# Create your views here.

def portfolio_detail(request,pk):
    project=Portfolio.objects.get(pk=pk)
    return render(request, 'landing_page/portfolio/portfolio_detail.html', {'project': project})