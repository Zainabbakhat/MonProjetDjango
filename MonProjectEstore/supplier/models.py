from django.db import models


class supplier(models.Model):
    
    nom_supplier= models.CharField(max_length=50)
    categorie_article=models.CharField(max_length=60)
    nom_article=models.CharField(max_length=60)
    quantite = models.DecimalField(max_digits=8, decimal_places=2)
    

    
