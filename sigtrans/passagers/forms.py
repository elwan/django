from django import forms
from passagers.models import Passager

class PassagerForm(forms.ModelForm):
    class Meta:
        model = Passager
        fields = ('nom','prenom','email','destination','vehicule','adresse','prix_transport','telephone',)
        
        
    
