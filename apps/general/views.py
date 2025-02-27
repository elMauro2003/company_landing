from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from .forms import *
from apps.portfolio.models import *

def index(request):
    hero = Hero.objects.first()
    about = About.objects.first()  # Asumiendo que solo hay una instancia de About
    alt_feature = AltFeatures.objects.all().order_by('pk')  # Asumiendo que solo hay una instancia de AltFeatures
    services = Services.objects.all().order_by('pk')  # Puede haber múltiples instancias de Services
    pricings = Pricing.objects.all().order_by('pk')
    portfolio = Portfolio.objects.all().order_by('pk')
    testimonials = Testimonials.objects.all().order_by('pk')
    teams = Team.objects.all().order_by('id')
    footer = Footer.objects.first()

    pricings_title = PricingSection.objects.first()
    portfolio_title = PortfolioSection.objects.first()
    testimonials_title = TestimonialSection.objects.first()
    team_title = TeamSection.objects.first()
    contact_title = ContactSection.objects.first()
    service_title = ServiceSection.objects.first()
    faq_title = FAQSection.objects.first()
   
    
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
        'footer': footer,
        
        'faq_title': faq_title,
        'pricings_title': pricings_title,
        'portfolio_title': portfolio_title,
        'testimonials_title': testimonials_title,
        'team_title': team_title,
        'contact_title': contact_title,
        'service_title': service_title,
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
        
        #print(terms_is_active)
        #for key, value in request.POST.items():
            #print(f"{key}: {value}")
        
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


def service_detail(request, slug):
    service = get_object_or_404(Services, slug=slug)
    faqs = service.faqs.all()
    
    is_service_detail = request.path.startswith('/service')
    context = {
        'faqs': faqs,
        'service': service,
        'is_service_detail': is_service_detail,
    }
    
    return render(request, 'landing_page/services/service_detail.html', context)

def get_started(request):
    term = Term.objects.first()
    conditions = TermPoint.objects.filter(term=term).order_by('pk')
    context = {
        'conditions': conditions
    }
    return render(request, 'started/contact.html', context)