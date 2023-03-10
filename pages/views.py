from django.shortcuts import render
from .models import *


def home(request):
   componentdump = ComponentDump.objects.all()
   navlinkitem = NavLinkItem.objects.select_related('navlink')
   testimonial = Testimonial.objects.all()
   aboutus = SectionBanner.objects.all()
   seo = SeoOptimization.objects.all()

   context = {
      'componentdump':componentdump,
      'navlinkitem':navlinkitem,
      'testimonial':testimonial,
      'aboutus':aboutus,
      'seo':seo,
      
   }

    
   return render(request, 'pages/index.html', context)