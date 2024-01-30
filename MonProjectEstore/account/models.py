from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Lien avec le modèle User de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Ajouter le champ typeofprofile
    TYPE_OF_PROFILE_CHOICES = [
        ('fournisseur', 'Fournisseur'),
        ('client', 'Client'),
    ]
    typeofprofile = models.CharField(max_length=100, choices=TYPE_OF_PROFILE_CHOICES)

    def __str__(self):
        return self.user.username

