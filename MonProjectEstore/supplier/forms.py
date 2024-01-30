from django import forms
from supplier.models import supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model=supplier
        fields="__all__"