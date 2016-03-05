from django.db import models
import random
import string 

# Create your models here.

class MiniUrl(models.Model):
    url = models.URLField(verbose_name='Mini url',unique=True)
    code = models.CharField(max_length=50,unique=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    nbre_acces=models.IntegerField(default=0)
    pseudo = models.CharField(max_length=100)
    
    def __str__(self):
        return "[{0}] {1}".format(self.code,self.url)

    def save(self,*args,**kwargs):
        if self.pk is None:
            self.generer(6)
        super(MiniUrl,self).save(*args,**kwargs)
    
    def generer(self,nb_caracteres):
        
        caracteres = string.ascii_letters + string.digits
        aleratoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        self.code= ''.join(aleratoire)

    class Meta:
        verbose_name="Mini Url"
        verbose_name_plural = "Minis Url"
        
       

    
    
