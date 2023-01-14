from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from decouple import config

def home(request):
   componentdump = ComponentDump.objects.all()
   navlinkitem = NavLink.objects.all()
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


@csrf_exempt
def whatsappHook(request):
   if request.method == 'GET':
      VERIFY_TOKEN = config('VERIFY_TOKEN')
      mode = request.GET['hub.mode']
      token = request.GET['hub.verify_token']
      challenge = request.GET['hub.challenge']

      if mode == 'subscribe' and token == VERIFY_TOKEN:
         return HttpResponse(challenge, status=200)

      else:
         return HttpResponse('error', status= 401)   

   if request.method == 'POST':
      data = json.loads(request.body)

      return HttpResponse('success', status= 200)

