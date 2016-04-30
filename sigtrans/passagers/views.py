from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from passagers.models import Passager
from django.core.urlresolvers import reverse_lazy
from passagers.forms import PassagerForm,VoyageForm

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


#crud views pour les voyages
class ListeVoyage(ListView):
    model = Voyage
    template_name = "passagers/voyage.html"
    context_object_name ="derniers_voyage"
    paginate_by = 6


class VoyageCreate(CreateView):
    model = Voyage
    template_name="passagers/add_voyage.html"
    form_class = VoyageForm
    success_url = reverse_lazy("liste_voyage")
    
class VoyageUpdate(UpdateView):
    model = Voyage
    template_name="passagers/add_voyage.html"
    form_class = VoyageForm
    success_url = reverse_lazy("liste_voyage")
    

class VoyageDelete(DeleteView):
    model = Voyage
    template_name = "passagers/delete_voyage.html"
    context_object_name="del_voyage"
    success_url = reverse_lazy("liste_voyage")
