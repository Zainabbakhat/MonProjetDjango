from django.db import models


class supplier(models.Model):
    
    nom_supplier= models.CharField(max_length=50, default='Supplier')
    categorie_article=models.CharField(max_length=60, default='Category')
    article=models.CharField(max_length=60, default='Product')
    quantite_article = models.DecimalField(max_digits=8, decimal_places=2)
    prix_unitaire= models.DecimalField(max_digits=999999999999, decimal_places=2, default="0.99") 

    

    
