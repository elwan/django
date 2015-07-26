from django.contrib import admin

# Register your models here.
from .models import  Question,Info,Categorie,SousCategorie,Reponse,Campagne,Vote,Region,Departement,Commune,Sms_recu

#admin.site.register(Campagne)
#admin.site.register(Localisation)
#admin.site.register(SousCategorie)
admin.site.register(Info)
#admin.site.register(Categorie)
#admin.site.register(Region)
#admin.site.register(Departement)
#admin.site.register(Commune)
admin.site.register(Sms_recu)

class Choix_reponse(admin.StackedInline):
    model=Reponse
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Questions',{'fields':['question_sms']}),
        ]
    inlines=[Choix_reponse]
admin.site.register(Question,QuestionAdmin)

#admin vote
class VoteLine(admin.StackedInline):
    model=Vote
    extra=1

class CampagneAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Campagnes',{'fields':['nom']}),
        #('Date publication',{'fields':['date_creation']}),
        ('Total vote ',{'fields':['nombre_total_vote']}),
        ]
    inlines = [VoteLine]
admin.site.register(Campagne,CampagneAdmin)

#admin localisation 
class DepartementLine(admin.StackedInline):
    model=Departement
    extra=1
class CommuneLine(admin.StackedInline):
    model = Commune
    extra =1 
class LocalisationAdmin(admin.ModelAdmin):
     fieldsets = [
         ('Regions',{'fields':['nom']}),
     ]
     inlines=[DepartementLine]
admin.site.register(Region,LocalisationAdmin)

class DepartementAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Departements',{'fields':['nom']}),
    ]
    inlines= [CommuneLine]
admin.site.register(Departement,DepartementAdmin)

#admin categories
class SouscatLine(admin.StackedInline):
    model=SousCategorie
    extra=1
class AdminCategorie(admin.ModelAdmin):
    fieldsets=[
         ('Categories',{'fields':['nom_categorie']}),
    ]
    inlines=[SouscatLine]
admin.site.register(Categorie,AdminCategorie)

 
