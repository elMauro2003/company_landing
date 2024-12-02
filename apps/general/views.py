from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    hero = Hero.objects.first()
    about = About.objects.first()  # Asumiendo que solo hay una instancia de About
    alt_feature = AltFeatures.objects.all()  # Asumiendo que solo hay una instancia de AltFeatures
    services = Services.objects.all()  # Puede haber múltiples instancias de Services
    pricings = Pricing.objects.all()
    portfolio = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()
    teams = Team.objects.all()
    filters = Filter.objects.all()
    
    return render(request, 'index.html', {
        'hero': hero,
        'about': about,
        'alt_feature': alt_feature,
        'services': services,
        'pricings': pricings,
        'projects': portfolio,
        'testimonials': testimonials,
        'teams': teams,
        'filters': filters,
    })

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Formulario enviado exitosamente!")
            response = render(request, 'landing_page/contact/contact.html', {'form': ContactForm()})
            response['HX-Trigger'] = 'contactAdded'
            return response
        else:
            return render(request, 'landing_page/contact/contact.html', {'form': form}, status=400)
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})