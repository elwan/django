from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,HttpResponse
from sva.forms import MessageForm
from sva.models import Message,Reponse,Pays_Destination,Message_Erreur
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required #Verification  des utilisateurs connectés pour les fonctions de vue 
#from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin #verification des utilisateurs connectés pour les built-in views
import nexmo 

# Create your views here.

#Creer une vue de formulaire avec la vue genereic createview
#@login_required(login_url="login/")
#method_decorator(login_required,name='dispatch')
class ListeMessage(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message
    context_object_name ="derniers_messages"
    template_name ="sva/messages.html"
    paginate_by = 10
    
class ListeMessageEnvoyes(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message
    context_object_name ="derniers_messages"
    template_name ="sva/messages_envoyes.html"
    paginate_by = 10
    
#@login_required(login_url="login/")
#@method_decorator(login_required,name='dispatch')
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
def envoi_message(request,code):
    client = nexmo.Client(key='852f8fa2',secret='aa4fcec9ead8902b') #Api de nexmo
    message=Message.objects.get(code=code)# recuper l'object à travers son code unique 
    numero=message.pays.indicatif_pays+message.numero # associer l'indicatif du pays avec le numéro de téléphone 
    numero_valide = numero.strip('+') # retirer le '+' devant l'indicatif 
    reponse=client.send_message({'from':message.sender,'to':numero_valide,'text':message.msg})#envoyer le message 
    #Enregistrer la réponse du message dans la base de donnée
    valide = reponse['messages'][0]['status']
    
    if valide == '0':  # Si le message est envoyé  enregistrer dans la base et changer son status 
        enregister_reponse(reponse,code)
        Message.objects.filter(code=code).update(status_message=True)
    else:                                        #sinon enregistrer le message d'erreur et retourer 
        enregister_message_erreur(reponse,code)  
    
    return render(request,'sva/envoi_sms.html',locals())
    #msg={'from':message.sender,'to':numero_valide,'text':message.msg}
    #return HttpResponse(msg.values())

def enregister_reponse(reponse,code):

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
def enregister_message_erreur(reponse,code):
    messaage_erreur = Message_Erreur()

    messaage_erreur.message_erreur=str(reponse['messages'][0]['error-text'])
    messaage_erreur.status= str(reponse['messages'][0]['status'])
    messaage_erreur.numero= str(reponse['messages'][0]['to'])
    messaage_erreur.code_message=code
    messaage_erreur.save()

    return True 
