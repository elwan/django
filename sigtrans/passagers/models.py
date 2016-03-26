from django.db import models

# Create your models here.
#modéles des passagers

class Destination(models.Model):
    depart=models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    def __str__(self):
        return "{0} --> {1}".format(self.depart,self.destination)
    
class Vehicule(models.Model):
    matricule=models.CharField(max_length=50)
    def __str__(self):
        return self.matricule  

class Comptabilite(models.Model):
    pass

class Voyage(models.Model):
    pass

class Passager(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    telephone = models.IntegerField(default=0)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    prix_transport = models.IntegerField(default=0)
    destination = models.ForeignKey(Destination)
    vehicule = models.ForeignKey(Vehicule)

    def __str__(self):
        return "{0} {1} {2}".format(self.nom,self.prenom,self.destination)

