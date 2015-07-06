from django.contrib import admin

# Register your models here.
from .models import  Question,Info,Localisation,Categorie,SousCategorie,Reponse

admin.site.register(Question)
admin.site.register(Localisation)
admin.site.register(SousCategorie)
admin.site.register(Info)
admin.site.register(Categorie)
admin.site.register(Reponse)

