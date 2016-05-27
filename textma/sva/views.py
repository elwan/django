from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,HttpResponse
from sva.forms import MessageForm
from sva.models import Message,Reponse,Pays_Destination,Message_Erreur
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required #Verification  des utilisateurs connectés pour les fonctions de vue 
#from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin #verification des utilisateurs connectés pour les class built-in views
import nexmo 

# Create your views here.

#views générique pour lister les messages enregistrés
#Toutes les classes  vues Génériques necessite un utilisateur logué pour pouvoir etre utiliser et ce grace à au premier paramettre LoginRequiredMixin 
#@login_required(login_url="login/")
class ListeMessage(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message
    context_object_name ="derniers_messages"
    template_name ="sva/messages.html"
    paginate_by = 10

#views générique pour lister  les messages Envoyés
class ListeMessageEnvoyes(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message
    context_object_name ="derniers_messages"
    template_name ="sva/messages_envoyes.html"
    paginate_by = 10
    

#views générique pour la creation  des messages
class MessageCreate(LoginRequiredMixin,CreateView):
    login_url='/login/'
    model = Message
    template_name = "sva/msgcreate.html"
    form_class = MessageForm
    success_url= reverse_lazy("lister_message")
    #Ajouter le usermane et le userid de l'utilisateur connecté 
    def form_valid(self,form):
        object=form.save(commit=False)
        object.utilisateur = self.request.user.username
        object.utilisateur_id= self.request.user.id 
        object.save()
        return super(MessageCreate,self).form_valid(form)
        
#views générique pour la mise à jour  des messages
class MessageUpdate(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model = Message
    template_name= "sva/msgcreate.html"
    form_class = MessageForm
    success_url = reverse_lazy("lister_message")

    def get_object(self,queryset=None):
        code= self.kwargs.get('code',None)

    def form_valid(self,form):
        self.object= form.save()

        return HttpResponseRedirect(self.get_success_url())

 #views générique pour la suppression des messages    
class MessageDelete(LoginRequiredMixin,DeleteView):
    login_url='/login/'
    model = Message
    context_object_name ="delete_message"
    template_name = "sva/deletemsg.html"
    success_url = reverse_lazy("lister_message")
    form_class = MessageForm

    def get_object(self,queryset=None):
        code= self.kwargs.get('code',None)
        return get_object_or_404(Message,code=code)


#fonction d'envoi de message
@login_required(login_url="/login/") 
def envoi_message(request,code):
    client = nexmo.Client(key='852f8fa2',secret='aa4fcec9ead8902b') #Api de nexmo
    message=Message.objects.get(code=code)# recuper l'object à travers son code unique 
    numero=message.pays.indicatif_pays+message.numero # associer l'indicatif du pays avec le numéro de téléphone 
    numero_valide = numero.strip('+') # retirer le '+' devant l'indicatif 
    reponse=client.send_message({'from':message.sender,'to':numero_valide,'text':message.msg})#envoyer le message 
    #Enregistrer la réponse du message dans la base de donnée
    valide = reponse['messages'][0]['status']
    
    if valide == '0':  # Si le message est envoyé  enregistrer dans la base et changer son status 
        enregister_reponse(request,reponse,code)
        Message.objects.filter(code=code).update(status_message=True)
    else:                                        #sinon enregistrer le message d'erreur et retourer 
        enregister_message_erreur(request,reponse,code)  
    
    return render(request,'sva/envoi_sms.html',locals())
    #msg={'from':message.sender,'to':numero_valide,'text':message.msg}
    #return HttpResponse(msg.values())

 #sauvegarder les reponses en cas d'envoi réussi du message
@login_required(login_url="/login/") 
def enregister_reponse(request,reponse,code):

    rep = Reponse()                                 #Créér un object reponse et remplir des elemets contenue dans le liste 
    rep.reseau=str(reponse['messages'][0]['network'])
    rep.cout_message=str(reponse['messages'][0]['message-price'])
    rep.message_id=str(reponse['messages'][0]['message-id'])
    rep.numero_telephone=str(reponse['messages'][0]['to'])
    rep.status_reponse=str(reponse['messages'][0]['status'])
    rep.credit_restant=str(reponse['messages'][0]['remaining-balance'])
    rep.compteur_message=str(reponse['message-count'])      #Mettre le deuxieme élément qui correspond à l'extraction du premier dict
    rep.code_message = code     #Mettre le code du message qui a été envoyer pour retrouver facile sa réponse 
    rep.save()  #Sauvegarder dans le base  

    return True

#Enregister les messages d'erreur quand le sms n'est pas envoyé

@login_required(login_url="/login/") 
def enregister_message_erreur(request,reponse,code):
    messaage_erreur = Message_Erreur()

    messaage_erreur.message_erreur=str(reponse['messages'][0]['error-text'])
    messaage_erreur.status= str(reponse['messages'][0]['status'])
    messaage_erreur.numero= str(reponse['messages'][0]['to'])
    messaage_erreur.code_message=code
    messaage_erreur.save()

    return True 
