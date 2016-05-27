from django.contrib import admin
from sva.models import Pays_Destination,Reponse,Message_Erreur,Message 

# Register your models here.
admin.site.register(Pays_Destination)
admin.site.register(Reponse)
admin.site.register(Message_Erreur)
admin.site.register(Message)

