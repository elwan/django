from django.db import models
from django.core.validators import RegexValidator 
# Create your models here.


class Pays_Destination(models.Model):
    nom_pays=models.CharField('Pays',max_length=25)
    indicatif_pays=models.CharField('Indicatif',max_length=4)

    def __str__(self):
        return " {0} {1}".format(self.nom_pays,self.indicatif_pays)


class Message(models.Model):
    numero = models.CharField('Numero Téléphone',max_length=9)
    sender=models.CharField('From',max_length=10)
    pays = models.ForeignKey(Pays_Destination)
    message=models.CharField('Message',max_length=160)
    utilisateurs=models.CharField('Utilisateur',max_length=20)
    status_message=models.BooleanField(default=False)
    Date=models.DateTimeField('Date',auto_now_add=True)

    def __str__(self):
        return "{0} {1} {3}".format(self.numero,self.message,self.sender)
    
    
