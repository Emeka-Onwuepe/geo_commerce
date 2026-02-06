from django import forms
from Branch.models import Cluster

from Product.models import  Category, Product, Product_Type, Size

class CategoryForm(forms.ModelForm):
    """Form definition for Category."""

    class Meta:
        """Meta definition for Categoryform."""

        model = Category
        fields = '__all__'
        

class SizeForm(forms.ModelForm):
    """Form definition for Size."""

    class Meta:
        """Meta definition for Sizeform."""

        model = Size
        fields = '__all__'

        
class ProductTypeForm(forms.ModelForm):
    """Form definition for Product_Type."""

    class Meta:
        """Meta definition for Product_Typeform."""

        model = Product_Type
        fields = '__all__'
        
class ProductForm(forms.ModelForm):
    """Form definition for Product."""
    sizes = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                queryset=Size.objects.all(),required=False)
    
    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = '__all__'
        

