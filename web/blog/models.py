from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom



class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur= models.CharField(max_length=50)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Date de parution")
    categorie=models.ForeignKey('Categorie')
    nb_vues=models.IntegerField(default=0)

    def __str__(self):
        return self.titre


class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    addresse=models.TextField()
    photo = models.ImageField(upload_to="photos/")

    def __str__(self):
        return self.nom
