from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from passagers.models import Passager
from django.core.urlresolvers import reverse_lazy
from passagers.forms import PassagerForm

# Create your views here.
#Crud view pour les passagers 
class ListePassager(ListView):
    model = Passager
    template_name = "passagers/accueil.html"
    context_object_name ="derniers_passager"
    paginate_by = 6


class PassagerCreate(CreateView):
    model = Passager
    template_name="passagers/add_passager.html"
    form_class = PassagerForm
    success_url = reverse_lazy("liste_passager")
    
class PassagerUpdate(UpdateView):
    model = Passager
    template_name="passagers/add_passager.html"
    form_class = PassagerForm
    success_url = reverse_lazy("liste_passager")
    

class PassagerDelete(DeleteView):
    model = Passager
    template_name = "passagers/delete_passager.html"
    context_object_name="del_passager"
    success_url = reverse_lazy("liste_passager")
