from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse,Http404
from datetime import datetime
from blog.models import Article,Membre
from blog.forms import ContactForm,ArticleForm,MembreForm
from django.views.generic import ListView, TemplateView,DetailView 

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

    
#def accueil (request):
    """ afficher tous les artciles de notre blog """
#    article = Article.objects.all()
#    return render(request,'blog/accueil.html',{'derniers_articles':article})

#def lire(request,id):
    """ afficher un article au complet"""
    #try:
    #    article=Article.objects.get(id=id)

    #except Article.DoesNotExist:
    #    raise Http404
#    article = get_object_or_404(Article,id=id)
#    return render(request,'blog/lire.html',{'article':article})


def contact(request):
    if request.method == 'POST': # s'il s'aggit d'une requete POST
        form = ContactForm(request.POST) #Nous reprennons les données
        
        if form.is_valid(): # Verifions que les donnees à envoyer sont valides

            #Maintenant nous pouvons traiter les données du formulaire
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur=form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            #Nous pourrions ici envoyer l'email grace au données collectées sur le formulaire

            envoi = True
            #return redirect(view_redirection)

    else: #Si ce n'est pas du POST ,c'est probablement du GET
        form = ContactForm() #Nous créons un formulaire vide


    
    return render(request, 'blog/contact.html',locals())


def articleform(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()   #sauvegarder l'article creer
            form=ArticleForm()
            envoi=True 

    else:
        form= ArticleForm()

    return render(request,'blog/articleform.html',locals())


def nouveau_membre(request):

    if request.method == 'POST':
        form = MembreForm(request.POST,request.FILES)
        if form.is_valid():
            #test=form.cleaned_data["nom"] #Recuperation des valeurs de du formulaire 
            form.save()
            sauvegarde = True
            form = MembreForm()

    else:
        form = MembreForm()

    return render(request,'blog/membre.html',locals())

#Les vues génériques avec template view
class FaqView(TemplateView):
    template_name= "blog/faq.html"  #Chemin vers le template a afficher
    
     
#Liste les artciles avec les vues generic en utilisant listview

class ListeArticles(ListView):
    model = Article
    context_object_name = "derniers_articles"
    template_name = "blog/accueil.html"
    paginate_by = 5


#Lire un article avec DetailView

class LireArticles(DetailView):
    model=Article
    context_object_name="article"
    template_name = "blog/lire.html"

    def get_object(self):
        #Recuper l'objet via la super-classe
        article=super(LireArticles,self).get_object()
        article.nb_vues +=1 #compter le nombre de vue 
        article.save()

        return article # retournns l'article 


#Afficher la liste des membre avec ListView des vues génériques

class ListeMembres(ListView):
    model=Membre
    template_name="blog/listmembre.html"
    context_object_name="derniers_membres"
    paginate_by=5


class LireMembres(DetailView):
    model = Membre
    context_object_name="membre"
    template_name="blog/liremembre.html"
    
