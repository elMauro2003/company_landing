from django.db import models
from solo.models import SingletonModel
from datetime import datetime

class Hero(SingletonModel):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='hero/')
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class About(SingletonModel):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class AltFeatures(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')
    def __str__(self):
        return self.title

class Services(models.Model):
    color = models.CharField(max_length=20, default='cyan')
    title = models.CharField(max_length=200)
    description = models.TextField(default='Available colors are: \n{ cyan, orange, teal, red, indigo, pink }')
    long_description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')
    button_text = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
class FAQ(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    column = models.BooleanField(default=0)
    service = models.ForeignKey(Services, related_name='faqs', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class FeatureService(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=255)
    portfolio = models.ForeignKey(Services, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Pricing(models.Model):
    plan_name = models.CharField(max_length=100)
    color = models.CharField(max_length=200, null=True)
    icon = models.CharField(max_length=200, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=3, null=True)
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.plan_name
    

class Testimonials(models.Model):
    client_name = models.CharField(max_length=200)
    stars = models.IntegerField(default=0)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    role = models.CharField(max_length=20, default='Cliente')
    
    def __str__(self):
        return self.client_name

class Team(models.Model):
    member_name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='team/')
    media1_url = models.URLField(blank=True, null=True)
    media1_icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')
    media2_url = models.URLField(blank=True, null=True)
    media2_icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')
    media3_url = models.URLField(blank=True, null=True)
    media3_icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')
    media4_url = models.URLField(blank=True, null=True)
    media4_icon = models.CharField(max_length=200, default='bi bi-cloud-download-fill')

    def __str__(self):
        return self.member_name

class Contact(models.Model):
    name = models.CharField( max_length=100,null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=350, null=True, blank=True)
    message = models.TextField(default='', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class ClientContact(models.Model):
    name = models.CharField( max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    email = models.EmailField()
    phone_number = models.IntegerField(null=False, blank=False)
    budget = models.DecimalField(max_digits=100, decimal_places=2, null=False, blank=False)
    budget_type = models.CharField(max_length=10, null=False, blank=False)
    service = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email