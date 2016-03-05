from django import forms
from mini_url.models import MiniUrl

class MiniUrlForm(forms.ModelForm):
    class Meta:
        model=MiniUrl
        fields =('url','pseudo')

        
