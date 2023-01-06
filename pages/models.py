from django.db import models
from tinymce.models import HTMLField
from meta.models import ModelMeta
from django.core.validators import MinValueValidator,FileExtensionValidator
from accounts.validators import validate_file_size
from django.urls import reverse 


class SeoOptimization(models.Model):
    seo_title = models.CharField(max_length=255)
    seo_keyword = models.TextField()

    def __str__(self):
        return self.seo_title

    def get_absolute_url(self):
        
        return reverse('home')      


class TopBar(models.Model):
    title = models.CharField(max_length=150)
    published = models.BooleanField(default=False)
    bar_src = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('home')      


class MainBanner(models.Model):
    title = models.CharField(max_length=150)
    published = models.BooleanField(default=False)
    banner_src = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse('home')      


class SectionBanner(models.Model):
    title = models.CharField(max_length=150)
    published = models.BooleanField(default=False)
    banner_src = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About us'   
        verbose_name_plural = 'About us'

    def get_absolute_url(self):
        
        return reverse('home')      

        
class ComponentDump(models.Model):
    title = models.CharField(max_length=150)
    body = HTMLField()

    def __str__(self):
        return self.title       

    def get_absolute_url(self):
        
        return reverse('home')      

class NavLink(models.Model):
    title = models.CharField(max_length=150)
    descriptions = models.TextField()     

    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        
        return reverse('home')      

     

class NavLinkItem(models.Model):        
    navlink = models.ForeignKey(NavLink, on_delete=models.CASCADE) 
    title = models.CharField(max_length=150)
    
    url_link = models.CharField(max_length=50)
    descriptions = models.TextField() 

    def __str__(self):
        return f'{self.navlink} - {self.title}'

    def get_absolute_url(self):
        
        return reverse('home')      

   

class Testimonial(models.Model):
    full_name = models.CharField(max_length=255)   
    position = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(default='logo-whitebg.jpg',upload_to = "pages/testimonials",validators=[validate_file_size, FileExtensionValidator(allowed_extensions=['png','jpg'])])                  


    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        
        return reverse('home')    