from django.db import models

# Create your models here.


class Filter(models.Model):
    filter_slug = models.CharField(max_length=50, default='filter-slug', blank=False, null=False, db_default='app')
    filter_name = models.CharField(max_length=50, default='Nombre Filtro', blank=False, null=False)
    
    def __str__(self):
        return self.filter_name
     

class Portfolio(models.Model):
    project_name = models.CharField(max_length=200)
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    #filter = models.CharField(max_length=100, blank=False, null=False, default='app')
    description = models.TextField()
    long_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='portfolio/')
    button1_text = models.CharField(max_length=100, blank=True, null=True)
    button2_text = models.CharField(max_length=100, blank=True, null=True)
    button2_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name
    
class FeaturePortfolio(models.Model):
    icon = models.CharField(max_length=80, default="bi bi-1-square-fill")
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=255)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class GalleryPortfolio(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name