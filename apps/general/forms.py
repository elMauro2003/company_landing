from django import forms
from .models import *

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['title', 'subtitle', 'background_image', 'button_text', 'button_link']

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'description', 'image', 'button_text', 'button_link']

class AltFeaturesForm(forms.ModelForm):
    class Meta:
        model = AltFeatures
        fields = ['title', 'description', 'icon']

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['color','title', 'description', 'icon', 'button_text', 'button_link']

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['plan_name', 'color', 'price', 'icon', 'date', 'button_text', 'button_link']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['project_name', 'filter', 'description', 'image', 'button1_text', 'button2_text', 'button2_link']

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['client_name', 'testimonial', 'image', 'stars', 'role']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['member_name', 'position', 'description', 'image', 'media1_url', 'media1_icon', 'media2_url', 'media2_icon', 'media3_url', 'media3_icon', 'media4_url', 'media4_icon']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'message']

class FilterForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = ['filter','filter_name']