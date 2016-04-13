from django.db import models

# Create your models here.
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


class Sms_envoyer(models.Model):
    numero = models.CharField(max_length=160)
    message = models.CharField(max_length=160)
    date_envoi = models.DateTimeField(auto_now_add=True)
    id_message_recu = models.CharField(max_length=10)

    def __str__(self):
        return " %s %s %s  "%(self.numero,self.message,self.id_message_recu)



class Lieu(models.Model):
    commune=models.CharField(max_length=20)
    def __str__(self):
        return "%s"%self.commune

class Sport(models.Model):
    nom=models.CharField(max_length=15)

    def __str__(self):
        return "%s" % self.nom
    
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length = 50)
    date_naissance = models.DateField()
    telephone = models.IntegerField(default=0)
    telephone2 = models.IntegerField(default=0)
    email = models.EmailField()
    adresse = models.CharField(max_length=20)
    lieu = models.ForeignKey('Lieu')
    sport_favori = models.ForeignKey('Sport')

    def __str__(self):
        return "%s %s %s %s"%(self.nom,self.prenom,self.telephone,self.lieu)
    

