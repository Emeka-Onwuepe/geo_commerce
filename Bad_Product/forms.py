from django import forms

from Bad_Product.models import Bad_Product

class BadProductForm(forms.ModelForm):
    """Form definition for BadProduct."""
    class Meta:
        """Meta definition for BadProductform."""

        model = Bad_Product
        fields = '__all__'
        

