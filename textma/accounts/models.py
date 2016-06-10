from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class Profile(AbstractUser):
    
    phone_regex = RegexValidator(regex=r'^7\d{8}$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    quota= models.IntegerField(default=0)
    nombre_sms_envoye=models.IntegerField(default=0)
    nombre_sms_restant=models.IntegerField(default=0)
    numero_telephone= models.CharField(validators=[phone_regex],unique=True,max_length=9)
    #date_naissance = models.DateField()

    REQUIRED_FIELDS=['numero_telephone','email']
    
