from django.db import models
from tinymce.models import HTMLField
from meta.models import ModelMeta
from django.core.validators import MinValueValidator,FileExtensionValidator
from accounts.validators import validate_file_size
from django.urls import reverse 
from accounts.models import Profile

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


class GetStarted(models.Model):
    title = models.CharField(max_length=50) 
    steps = models.TextField(verbose_name='Get Started Steps')


    def __str__(self):
        return self.title



class OurRate(models.Model):
    coins_type_choices = (
         ('BTC', 'BTC'),
        ('ETH', 'ETH'),
        ('DODGE', 'DODGE')
    )
    coins_name = models.CharField(max_length=50,choices=coins_type_choices)
    bulk_quantity = models.CharField(max_length=50, help_text=('$0 - $50'))
    exchange_rate = models.CharField(max_length=250, help_text=('750NGN'))
    as_at = models.DateTimeField()
    updated_as_at = models.DateField(auto_now=True)

class ChatSession(models.Model):
    trading_type_choices = (
        ('BTC', 'BTC'),
        ('ETH', 'ETH'),
        ('DODGE', 'DODGE')
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    init = models.CharField(max_length=50,blank=True,null=True)
    trading_type = models.CharField(max_length=50, choices=trading_type_choices,blank=True,null=True)
    our_rate = models.ForeignKey(OurRate, on_delete=models.CASCADE)
    trade_rite_wallet = models.CharField(max_length=250, blank=True,null=True)
    client_wallet = models.CharField(max_length=250,blank=True,null=True)
    bank_account_number = models.CharField(max_length=250,blank=True,null=True)
    bank_account_name = models.CharField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.profile


