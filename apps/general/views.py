from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from .forms import *
from apps.portfolio.models import *

def index(request):
    hero = Hero.objects.first()
    about = About.objects.first()  # Asumiendo que solo hay una instancia de About
    alt_feature = AltFeatures.objects.all()  # Asumiendo que solo hay una instancia de AltFeatures
    services = Services.objects.all()  # Puede haber múltiples instancias de Services
    pricings = Pricing.objects.all().order_by('pk')
    portfolio = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()
    teams = Team.objects.all()
    #filters = Filter.objects.all()
    
    # Sacar los filtros
    filters = set()
    for project in portfolio:
        filters.add(project.filter)
        
    
    current_url = request.path
    
    return render(request, 'index.html', {
        'current_url': current_url,
        'hero': hero,
        'about': about,
        'alt_feature': alt_feature,
        'services': services,
        'pricings': pricings,
        'projects': portfolio,
        'testimonials': testimonials,
        'teams': teams,
        'filters': filters,
        'current_url': current_url,
    })

def create_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulario enviado exitosamente!")
            response = render(request, 'landing_page/contact/contact_response.html', {'form': ContactForm()})
            response['HX-Trigger'] = 'contactAdded'
            return response
    return render(request, 'landing_page/contact/contact_response.html', {'form': form})

def client_contact(request):
    form = ClientContactForm()
    if request.method == 'POST':
        form = ClientContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulario enviado exitosamente!")
            response = render(request, 'started/contact_response.html', {'form': ClientContactForm()})
            response['HX-Trigger'] = 'contactAdded'
            return response
        else:
            messages.error(request, "Error al enviar el formulario")
            return render(request, 'started/contact_response.html', {'form': form})
        
    return render(request, 'started/contact_response.html', {'form': form})


def service_detail(request, pk):
    service = Services.objects.get(pk=pk)
    faqs = service.faqs.all()
    
    is_service_detail = request.path.startswith('/service-detail')
    context = {
        'faqs': faqs,
        'service': service,
        'is_service_detail': is_service_detail,
    }
    
    return render(request, 'landing_page\services\service_detail.html', context)

def get_started(request):
    return render(request,'started/contact.html')