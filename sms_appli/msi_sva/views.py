from django.shortcuts import render,HttpResponse 
from msi_sva.models import Sms_recu
# Create your views here.

def test(request,msg):
    #text= "test de vue"
    return HttpResponse(msg)


def save_sms(request,id_message,numero_court,numero_telephone,msg,date_reception,mot_cle):
    
    message=Sms_recu()
    message.numero=int(numero_telephone)
    message.id_message=int(id_message)
    message.mot_cle=mot_cle
    message.message_text=msg
    message.numero_court=int(numero_court)
    message.date_reception=date_reception
    message.save()

    #return HttpResponse("{0} {1} {2} {3} {4} {5}".format(id_message,numero_telephone,numero_court,message,date_reception,mot_cle))
    return HttpResponse(msg)


def router_sms(request,msg):

    message = msg
    messages = message.split('+')
    
    pass


def envoyer_sms(request,numero,message,context):
    
    pass

def inscription(request):

    pass

def vote(request):

    pass 



