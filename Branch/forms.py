from django import forms
from Branch.models import (Cluster, Cluster_Product, Product_Size)

class clusterForm(forms.ModelForm):
                            
    class Meta:
        model = Cluster
        fields = '__all__'
        
class clusterProductForm(forms.ModelForm):
    """Form definition for clusterProduct."""

    class Meta:
        """Meta definition for clusterProductform."""

        model = Cluster_Product
        fields = '__all__'

class ProductSizeForm(forms.ModelForm):
    """Form definition for ProductSize."""

    class Meta:
        """Meta definition for ProductSizeform."""

        model = Product_Size
        fields = '__all__'