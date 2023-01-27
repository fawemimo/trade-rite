from django.shortcuts import render

from pages.whatsapp import handleWhatsappChat, sendWhatsappMessage
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
   banner = MainBanner.objects.all()
   get_started = GetStarted.objects.all()

   context = {
      'componentdump':componentdump,
      'navlinkitem':navlinkitem,
      'testimonial':testimonial,
      'aboutus':aboutus,
      'seo':seo,
      'banner':banner,
      'get_started':get_started
      
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
         return HttpResponse('error', status= 403)   

   if request.method == 'POST':
      data = json.loads(request.body)
      if 'object' in data and 'entry' in data:
         if data['object'] == 'whatsapp_business_account':
            
            for entry in data['entry']:
               mobile = entry['changes'][0]['value']['metadata']['display_phone_number']
               phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
               profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
               whatsAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
               fromId = entry['changes'][0]['value']['messages'][0]['from']
               messageId = entry['changes'][0]['value']['messages'][0]['id']
               timestamp = entry['changes'][0]['value']['messages'][0]['text']['body']
               text = entry['changes'][0]['value']['messages'][0]['text']['body']


               mobile = '2348058367768'
               message = 'RE: {} was received'.format(text)

               handleWhatsappChat(fromId, profileName,phoneId,text)
         else:
            pass
      else:
         pass                

      return HttpResponse('success', status= 200)

