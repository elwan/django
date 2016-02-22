from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse,Http404
from datetime import datetime
from blog.models import Article


# Create your views here.

def home(request):
    text="""<h1> Bienvenue sur mon blog les amis ! </h1>"""
    return HttpResponse(text)


def vue_article(request,id_article):
    if int(id_article) > 10:
        return redirect(view_redirection)
    else:
        text = "vous avez demander le l'article #{0} !".format(id_article)
        return HttpResponse(text)

def view_redirection(request):
    return HttpResponse("Vous avew été redirigé.")

def calcul(request,nbr1,nbr2):
    if int(nbr1)==0 and int(nbr2) == 0 :
        raise Http404
    resultat = " {0} + {1} = {2} ".format(nbr1,nbr2,int(nbr1)+int(nbr2))
    return HttpResponse(resultat)

def heure_actuelle(request):
    return render(request,'blog/date.html',{'date':datetime.now()})

def division(request,nbr1,nbr2):
    if int(nbr2)== 0 :
        raise Http404
    else:

        resultat = int(nbr1) / int(nbr2)
        
        return render(request,'blog/division.html',locals())

    
def accueil (request):
    """ afficher tous les artciles de notre blog """
    article = Article.objects.all()
    return render(request,'blog/accueil.html',{'derniers_articles':article})

def lire(request,id):
    """ afficher un article au complet"""
    #try:
    #    article=Article.objects.get(id=id)

    #except Article.DoesNotExist:
    #    raise Http404
    article = get_object_or_404(Article,id=id)
    return render(request,'blog/lire.html',{'article':article})




