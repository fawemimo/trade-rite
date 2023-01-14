from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('2b55ba09-aa70-4625-a91d-8055405a0fae/', views.whatsappHook,name='whatsapp-hook'),
]

# Token - 07850b98-a418-41e0-89e0-2eb696f8c095