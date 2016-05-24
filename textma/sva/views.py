from django.shortcuts import render,HttpResponseRedirect,get_object_or_404
from sva.forms import MessageForm
from sva.models import Message
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
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
    paginate_by = 5 
#@login_required(login_url="login/")
#@method_decorator(login_required,name='dispatch')
class MesssageCreate(LoginRequiredMixin,CreateView):
    login_url='/login/'
    model = Message
    template_name = "sva/msgcreate.html"
    form_class = MessageForm
    success_url= reverse_lazy("lister_message")

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
def envoi_sms():
    pass 
    
