from django.db import models
from Branch.models import Cluster

from Product.models import Product, Size


# Create your models here.

class Returned_Product_Abstract(models.Model):
    """Model definition for Returned_Product_Abstract."""

    # TODO: Define fields here
    qty = models.IntegerField("qty",null=False,blank=False)
    unit_price = models.DecimalField("unit_price", max_digits=50, decimal_places=2,null=False,blank=False)
    total_price = models.DecimalField("total_price", max_digits=50, decimal_places=2,null=False,blank=False) 
    date_of_purchase = models.DateField("date_of_purchase", auto_now=False, auto_now_add=False,null=False,blank=False)
    date_of_return = models.DateTimeField("date_of_return", auto_now=False, auto_now_add=False,null=False,blank=False)

    class Meta:
        """Meta definition for Returned_Product_Abstract."""
        abstract = True

      

class Returned_Product(Returned_Product_Abstract):
    """Model definition for Returned_Product."""

    # TODO: Define fields here
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name = "returned_product_product_type")
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name="returned_product_cluster")
    size_instance = models.ForeignKey(Size, verbose_name="size_instance", on_delete=models.CASCADE,
                        related_name="returned_product_size_instance",null=True, blank=True)

    class Meta:
        """Meta definition for Returned_Product."""

        verbose_name = 'Returned_Product'
        verbose_name_plural = 'Returned_Products'

    def __str__(self):
        """Unicode representation of Returned_Product."""
        return f" {self.cluster} - {self.product} - {self.total_price}"