from django.shortcuts import render
from django.views.generic import ListView
from passagers.models import Passager

# Create your views here.

class ListePassager(ListView):
    model = Passager
    template_name = "passagers/accueil.html"
    context_object_name ="derniers_passager"

    
