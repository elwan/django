from django import forms
from passagers.models import Passager,Voyage

class PassagerForm(forms.ModelForm):
    class Meta:
        model = Passager
        fields = ('nom','prenom','email','adresse','prix_transport','telephone',)

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ('vehicule','passager','numero','destination',)


        
        
    
