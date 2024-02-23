from django import forms
from supplier.models import supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        fields = ['nom_supplier', 'categorie_article', 'article', 'quantite_article', 'prix_unitaire']


        
