from django import forms
from .models import DeliveryInfo

class DeliveryInfoForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ['addresse', 'code_postal', 'ville', 'pays']
        # Vous pouvez ajouter des widgets ici pour personnaliser la façon dont les champs sont affichés
