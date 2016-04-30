from django.db import models

# Create your models here.
#modéles des passagers

class Destination(models.Model):
    depart = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    def __str__(self):
        return "{0} --> {1}".format(self.depart,self.destination)

class TypeVehicule(models.Model):
      nom = models.CharField(max_length=20)
      nombre_place=models.IntegerField(default=1)
      poids_vehicule_vide=models.IntegerField(default=1)
      poids_vehicule_charge=models.IntegerField(default=2)

      def __str__(self):
          return "{0} {1} ".format(self.nom,self.nombre_place)
      
class Vehicule(models.Model):
    #nbreplace=models.IntegerField(default=0)
    categorie = models.ForeignKey('TypeVehicule',on_delete=models.CASCADE)
    matricule=models.CharField(max_length=50,primary_key=True)
    
    def __str__(self):
        return self.matricule  

class Comptabilite(models.Model):
    pass


class Passager(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)
    telephone = models.IntegerField(default=0)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    prix_transport = models.IntegerField(default=0)
    #destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    #vehicule = models.ForeignKey(Vehicule)

    def __str__(self):
        return "{0} {1} {2}".format(self.nom,self.prenom,self.destination)

class Voyage(models.Model):
    date= models.DateTimeField(auto_now_add=True)
    vehicule=models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    passager = models.ForeignKey(Passager,on_delete=models.CASCADE)
    numero = models.IntegerField()
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)
    
    def __str__(self):
        return " {0} {1} {2}".format(self.date,self.vehicule,self.numero,self.destination)

