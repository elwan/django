from django.db import models
from django.core.validators import RegexValidator
import random
import string
# Create your models here.


class Pays_Destination(models.Model):
    nom_pays=models.CharField('Pays',max_length=25)
    indicatif_pays=models.CharField('Indicatif',max_length=4)
    prix_sms = models.IntegerField(default=0)

    def __str__(self):
        return " {0} {1}".format(self.nom_pays,self.indicatif_pays)


class Message(models.Model):
    phone_regex = RegexValidator(regex=r'^7\d{8}$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    numero = models.CharField('Numero Téléphone',validators=[phone_regex],max_length=9)
    sender=models.CharField('From',max_length=10)
    pays = models.ForeignKey(Pays_Destination)
    msg=models.TextField('Message',max_length=160)
    utilisateur=models.CharField('Utilisateur',max_length=20)
    utilisateur_id=models.IntegerField(default=0)
    status_message=models.BooleanField(default=False)
    date=models.DateTimeField('Date',auto_now_add=True)
    code=models.CharField('Code',max_length=15)

    def __str__(self):
        return "{0} {1} {2}".format(self.numero,self.msg,self.sender)

    def save(self,*args,**kwargs):
        if self.pk is None:
            self.code_generator(6)
            #self.utilisateur=request.username
        super(Message,self).save(*args,**kwargs)

    def code_generator(self,nb_caractere):
        car = string.ascii_letters + string.digits
        aleatoire = [random.choice(car) for _ in range(nb_caractere)]

        self.code =''.join(aleatoire)

 #  sauvegarde de tous les reponses des messages qui sont envoyés via nexmo    
class Reponse(models.Model):
    reseau= models.CharField('Reseau',max_length=10)
    cout_message=models.CharField('Prix_message',max_length=5)
    message_id= models.CharField('Message_id',max_length=15)
    numero_telephone=models.CharField('Numero de Téléphone',max_length=15)
    status_reponse=models.CharField('Status',max_length=10)
    credit_restant=models.CharField('Crédit restant',max_length=5)
    compteur_message=models.CharField('Compteur Message',max_length=10)
    code_message= models.CharField('Code Message',max_length=6)
    date_reponse= models.DateTimeField('Date',auto_now_add=True)

    def __str__(self):
        return "{0} {1} {2}".format(self.numero_telephone,self.credit_restant,self.status_reponse)
    
    
