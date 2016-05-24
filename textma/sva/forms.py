from django import forms
from sva.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=('numero','sender','msg','pays','utilisateur')


        
