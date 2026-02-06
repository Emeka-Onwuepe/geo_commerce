from django import forms

from Returned_Product.models import Returned_Product


class ReturnedProductForm(forms.ModelForm):
    """Form definition for ReturnedProduct."""

    class Meta:
        """Meta definition for ReturnedProductform."""

        model = Returned_Product
        fields = '__all__'
        widgets = {
            "date_of_purchase" : forms.widgets.DateInput(attrs={'type':'date'}),
            "date_of_return"  : forms.widgets.DateInput(attrs={'type':'date'})     
        }
  