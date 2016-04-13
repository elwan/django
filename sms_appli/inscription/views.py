from django.shortcuts import render,HttpResponse
from inscription.models import Utilisateur,Sms_recu,Sms_envoyer,Lieu

# Create your views here.

def save_sms(request,id_msg,sc,numero,msg,date,key):

    sms = Sms_recu()
    sms.id_message=id_msg
    sms.numero = numero
    sms.message = msg
    sms.date_reception = date
    sms.mot_cle = key
    sms.numero_court = sc
    sms.save()

    return  HttpResponse(sms.numero)


def  process_sms(request,id_msg,message,numero):

    msg = message.strip(' ').split(' ')
    if len(msg) == 4 :
        user = Utilisateur()
        user.nom = user[0]
        user.prenom = user[1]
        user.commune=user[2]
        user.sport_favori = user[3]
        user.telephone=numero
        user.save()
    else:
        pass
    return HttpResponse("OK")

    
