from django.conf import settings
import requests
from accounts.models import Profile, User
from pages.models import ChatSession, OurRate
from django.db import transaction


def sendWhatsappMessage(phoneNumber,message):
    headers = {'Authorization': settings.WHATSAPP_TOKEN}
    payload = {'messaging_product': 'whatsapp',
                'recipient_type':'individual',
                'to':phoneNumber,
                'type':'text',
                'text': {'body':message}
            }
    response = requests.post(settings.WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()
    # return ans


def handleWhatsappChat(fromId,profileName, phoneId,text):
    try:     
        chat = ChatSession.objects.get(profile__phoneNumber=fromId)
    except:
        # create a user if is None
        if User.objects.filter(username=phoneId).exists():
            user = User.objects.get(username=phoneId)
            profile = user.profile
        else:    
            user =  User.objects.create_user(username=phoneId, email='help@trade-rite.ng',password='password',name=profileName)

            # create the profile
            profile = Profile.objects.create(user=user,phoneNumber=fromId,phoneID=phoneId)

        # create the chat session
        chat = ChatSession.objects.create(profile=profile)
        message = 'Welcome to Trade-rite where you can get your coins at very high rates and swift payment, type anything to continue trading'
        sendWhatsappMessage(fromId, message)
        return ''

    if chat.init:
        if chat.trading_type:
            pass
        else:
            with transaction.atomic():
                try:
                    type = int(text.replace(' ',''))
                    if type == 1:
                        chat.trading_type = 'BTC'
                        chat.save()
                        our_rate = OurRate.objects.filter(coins_name='BTC')
                        list_rate = [(x.bulk_quantity ,x.exchange_rate, x.updated_as_at )for x in our_rate]
                        message = f' Here is our rate for BTC only \n {list_rate} \n Or ask for rate from the Admin by dialing +2348058467768'
                        sendWhatsappMessage(fromId,message)
                        return ''   
                    elif type == 2    :
                        chat.trading_type = 'ETH'
                        chat.save()
                        our_rate = OurRate.objects.filter(coins_name='ETH')
                        list_rate = [(x.bulk_quantity ,x.exchange_rate, x.updated_as_at )for x in our_rate]
                        message = f' Here is our rate for ETH only \n {list_rate} \n Or ask for rate from the Admin by dialing +2348058467768'
                        sendWhatsappMessage(fromId,message)
                        return ''
                    elif type == 3   :
                        chat.trading_type = 'DODGE'
                        chat.save()
                        our_rate = OurRate.objects.filter(coins_name='DODGE')
                        list_rate = [(x.bulk_quantity ,x.exchange_rate, x.updated_as_at )for x in our_rate]
                        message = f' Here is our rate for DODGE only \n {list_rate} \n Or ask for rate from the Admin by dialing +2348058467768'
                        sendWhatsappMessage(fromId,message)  
                        return ''
                    else:
                        message = 'Please try again, Enter the correct number: \n 1. BTC \n 2. ETH \n 3. DODGE \n To see the latest rate as at now'   
                        sendWhatsappMessage(fromId, message)
                        return ''

                except:
                    message = 'Please try again, Enter the correct number: \n 1. BTC \n 2. ETH \n 3. DODGE \n To see the latest rate as at now'   
                    sendWhatsappMessage(fromId, message)
                    return ''

    else:
        chat.init = text
        chat.save()

        message = 'Please select the trading type you wish to transact with us'
        sendWhatsappMessage(fromId, message)
        return ''