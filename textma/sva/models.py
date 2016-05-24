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
    msg=models.CharField('Message',max_length=160)
    utilisateur=models.CharField('Utilisateur',max_length=20)
    status_message=models.BooleanField(default=False)
    date=models.DateTimeField('Date',auto_now_add=True)
    code=models.CharField('Code',max_length=15)

    def __str__(self):
        return "{0} {1} {2}".format(self.numero,self.msg,self.sender)

    def save(self,*args,**kwargs):
        if self.pk is None:
            self.code_generator(6)
        super(Message,self).save(*args,**kwargs)

    def code_generator(self,nb_caractere):
        car = string.ascii_letters + string.digits
        aleatoire = [random.choice(car) for _ in range(nb_caractere)]

        self.code =''.join(aleatoire)

    
