from django import forms
from blog.models import Article,Membre


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur= forms.EmailField(label="votre adresse email")
    renvoi = forms.BooleanField(help_text="Cochew si vous souhautez obtenir une copie u mail envoyé",required=False)

    def clean_message(self):
        message= self.cleaned_data['message']
        if "mariage" in message:
            raise forms.ValidationError("On ne veut pas entendre de mariage ici")
        return message


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=('titre','auteur','contenu','categorie')
        

        
class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields =('nom','prenom','addresse','photo')
        
