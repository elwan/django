from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Question(models.Model):
    question_sms=models.CharField('Question',max_length=200,unique=True)
    date_pub=models.DateTimeField('date creation',auto_now_add=True)
    def __str__(self):
        return self.question_sms

class Reponse(models.Model):
    question=models.ForeignKey(Question,verbose_name="Question")
    reponse_sms=models.CharField('Reponse',max_length=160)
    #def clean(self):
        #self.reponse_sms = self.reponse_sms.capitalize()
    #    pass
    def __str__(self):
        return self.reponse_sms

#model information  sera lier a une categories et une localisation
  
class Categorie(models.Model):
    nom_categorie=models.CharField(max_length=100,unique=True)
    date_creation=models.DateTimeField('date creation',auto_now_add=True)
    #case sensivity in input data 
    def clean(self):
                self.nom_categorie = self.nom_categorie.capitalize()
    
    def __str__(self):
        return self.nom_categorie
    
class SousCategorie(models.Model): 
    nom_sous_categorie=models.CharField(max_length=100,unique=True)
    categorie=models.ForeignKey(Categorie)
    date_creation=models.DateTimeField('date creation',auto_now_add=True)
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
    date_campagne=models.DateTimeField('Date creation',auto_now_add=True)

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
    date_vote=models.DateTimeField('Date creation ',auto_now_add=True)
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

class Departement(models.Model):
    nom = models.CharField(max_length=50,unique=True)
    region =models.ForeignKey(Region)
    def clean(self):
        self.nom =self.nom.capitalize()
    def __str__(self):
        return " %s " %(self.nom)        
class Commune(models.Model):
    nom = models.CharField(max_length=50,unique=True)
    departement = models.ForeignKey(Departement)
    def clean(self):
        self.nom =self.nom.capitalize()
    def __str__(self):
        return " %s " %(self.nom)

#classe information 
class Info(models.Model):
    nom =models.CharField('Nom Service',max_length=20,primary_key=True,unique=True)
    adresse=models.CharField('Adresse',max_length=50)
    phone_regex = RegexValidator(regex=r'^7\d{8}$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    #telephone_mobile =models.IntegerField()
    telephone_mobile = models.CharField('Mobile',validators=[phone_regex],blank=True,max_length=9)
    phone_fix_regex = RegexValidator(regex=r'^3\d{8}$', message="Phone number must be entered in the format: '3xxxxxxxx'. Up to 9 digits allowed.")
    #telephone_fixe=models.IntegerField()
    telephone_fixe=models.CharField('Telephone Fixe',validators=[phone_fix_regex],blank=True,max_length=9)
    email=models.EmailField('Email')
    site_web=models.URLField('Site web',max_length=50,blank=True)
    categorie=models.ForeignKey(SousCategorie,verbose_name="Caterogie de service")
    localisation=models.ForeignKey(Commune)
    date_creation=models.DateTimeField('date creation',auto_now_add=True)
    tagline = models.TextField('Tags',max_length=255,blank=True)

    def clean(self):
                self.nom = self.nom.capitalize()

    def __str__(self):
        return " %s  %s  %s " % (self.nom ,self.adresse,str(self.telephone_mobile))       

#model pour enregister tous les messsages recus 
class Sms_recu(models.Model):
    numero = models.CharField(max_length=15)
    message_text=models.CharField(max_length=160)
    id_message=models.IntegerField()
    numero_court=models.IntegerField()
    date_reception=models.CharField(max_length=10)
    date_enregistrement=models.DateTimeField(auto_now_add=True)
    mot_cle=models.CharField(max_length=10)
    def __str__(self):
        return  "%s %s %s %s %s %s %s" % (self.numero,self.message_text,str(self.id),str(self.numero_court),self.date_reception,self.date_enregistrement,self.mot_cle) 

    
