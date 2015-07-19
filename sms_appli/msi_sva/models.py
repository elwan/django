from django.db import models

# Create your models here.


class Question(models.Model):
    question_sms=models.CharField(max_length=200,unique=True)
    date_pu=models.DateTimeField('date creation')
    def __str__(self):
        return self.question_sms

class Reponse(models.Model):
    question=models.ForeignKey(Question)
    reponse_sms=models.CharField(max_length=160,unique=True)
    def clean(self):
        self.reponse_sms = self.reponse_sms.capitalize()
    def __str__(self):
        return self.reponse_sms

#model information  sera lier a une categories et une localisation
  
class Categorie(models.Model):
    nom_categorie=models.CharField(max_length=100,unique=True)
    date_creation=models.DateTimeField('date creation')
    #case sensivity in input data 
    def clean(self):
                self.nom_categorie = self.nom_categorie.capitalize()
    
    def __str__(self):
        return self.nom_categorie
    
class SousCategorie(models.Model): 
    nom_sous_categorie=models.CharField(max_length=100,unique=True)
    categorie=models.ForeignKey(Categorie)
    date_creation=models.DateTimeField('date creation')
    def clean(self):
                self.nom_sous_categorie = self.nom_sous_categorie.capitalize()
    
    def __str__(self):
        return self.nom_sous_categorie

#class Localisation(models.Model):
#    nom_zone=models.CharField(max_length=100,unique=True)
#    date_creation=models.DateTimeField('date creation')

#    def __str__(self):
#        return self.nom_zone
    
#systeme de vote
class Campagne(models.Model):
    nom = models.CharField(max_length=100,unique=True)
    date_creation= models.DateTimeField()
    nombre_total_vote = models.IntegerField(default=0)

    def clean(self):
                        self.nom = self.nom.capitalize()
    #def clean(self):
    #    self.nom = self.nom.capitalize()

    def __str__(self):
        return " %s %s " % (self.nom,str(self.nombre_total_vote))
class Vote(models.Model):
    campagne=models.ForeignKey(Campagne)
    nom_candidat= models.CharField(max_length=20,unique=True)
    id_candidat = models.CharField(max_length=5,unique=True)
    votes= models.IntegerField(default=0)
    def clean(self):
        self.nom_candidat = self.nom_candidat.capitalize()
        self.id_candidat = self.id_candidat.capitalize()
    def __str__(self):
        return " %s %s " % (self.nom_candidat,str(self.id_candidat))

class Region(models.Model):
    nom=models.CharField(max_length=50,unique=True)
    def clean(self):
        self.nom =self.nom.capitalize()
    def __str__(self):
        return " %s " %(self.nom)

class Departemant(models.Model):
    nom = models.CharField(max_length=50,unique=True)
    region =models.ForeignKey(Region)
    def clean(self):
        self.nom =self.nom.capitalize()
    def __str__(self):
        return " %s " %(self.nom)        
class Commune(models.Model):
    nom = models.CharField(max_length=50,unique=True)
    departemant = models.ForeignKey(Departemant)
    def clean(self):
        self.nom =self.nom.capitalize()
    def __str__(self):
        return " %s " %(self.nom)

#classe information 
class Info(models.Model):
    nom =models.CharField(max_length=20,primary_key=True,unique=True)
    adresse=models.CharField(max_length=50)
    telephone_mobile =models.IntegerField()
    telephone_fixe=models.IntegerField()
    email=models.EmailField()
    categorie=models.ForeignKey(SousCategorie)
    localisation=models.ForeignKey(Commune)
    date_creation=models.DateTimeField('date creation')

    def clean(self):
                self.nom = self.nom.capitalize()

    def __str__(self):
        return " %s  %s  %s " % (self.nom ,self.adresse,str(self.telephone_mobile))       


