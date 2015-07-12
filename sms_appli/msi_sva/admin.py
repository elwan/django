from django.contrib import admin

# Register your models here.
from .models import  Question,Info,Localisation,Categorie,SousCategorie,Reponse,Campagne,Vote

#admin.site.register(Campagne)
admin.site.register(Localisation)
admin.site.register(SousCategorie)
admin.site.register(Info)
admin.site.register(Categorie)
#admin.site.register(Vote)

class Choix_reponse(admin.StackedInline):
    model=Reponse
    extra=1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['question_sms']}),
        ('Date publication',{'fields':['date_pu'],'classes':['collapse']}),
        ]
    inlines=[Choix_reponse]
admin.site.register(Question,QuestionAdmin)

#admin vote
class VoteLine(admin.StackedInline):
    model=Vote
    extra=1

class CampagneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields':['nom']}),
        ('Date publication',{'fields':['date_creation']}),
        ('Total vote ',{'fields':['nombre_total_vote']}),
        ]
    inlines = [VoteLine]
admin.site.register(Campagne,CampagneAdmin)




 
