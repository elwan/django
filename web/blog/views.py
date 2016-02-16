from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def home(request):
    text="""<h1> Bienvenue sur mon blog les amis ! </h1>"""
    return HttpResponse(text)


def vue_article(request,id_article):
    text = "vous avez demander le l'article #{0} !".format(id_article)
    return HttpResponse(text)

def calcul(request,nbr1,nbr2):
    if int(nbr1)==0 and int(nbr2) == 0 :
        raise Http404
    resultat = " {0} + {1} = {2} ".format(nbr1,nbr2,int(nbr1)+int(nbr2))
    return HttpResponse(resultat)
