from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DeliveryInfo(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    addresse = models.CharField(max_length=1024)
    code_postal = models.CharField(max_length=12)
    ville = models.CharField(max_length=1024)
    pays = models.CharField(max_length=1024)
  
