from django import forms

from Stock.models import Product_Stock


class ProductStockForm(forms.ModelForm):
    """Form definition for ProductStock."""

    class Meta:
        """Meta definition for ProductStockform."""

        model = Product_Stock
        fields = '__all__'