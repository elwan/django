from django.contrib import admin
from  passagers.models import Passager,Vehicule,Destination,Voyage,TypeVehicule


# Register your models here.

admin.site.register(Passager)
admin.site.register(Vehicule)
admin.site.register(Destination)
admin.site.register(Voyage)
admin.site.register(TypeVehicule)
