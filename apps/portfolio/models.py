from django.db import models

# Create your models here.


class Filter(models.Model):
    filter = models.CharField(max_length=50, default='nombre_filtro', blank=False, null=False)
    filter_name = models.CharField(max_length=50, default='Filtro', blank=False, null=False)
    
    def __str__(self):
        return self.filter_name
    
    

class Portfolio(models.Model):
    project_name = models.CharField(max_length=200)
    filter = models.CharField(max_length=100, blank=False, null=False, default='app')
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    button1_text = models.CharField(max_length=100, blank=True, null=True)
    button2_text = models.CharField(max_length=100, blank=True, null=True)
    button2_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name