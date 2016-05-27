from django import forms
from sva.models import Message,Pays_Destination

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=('numero','sender','msg','pays')




        
