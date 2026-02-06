from typing import Any
from django.db import models
from Branch.models import Cluster
from Product.models import Product, Size, Size

# Create your models here.
   
class Stock(models.Model):
    """Model definition for Product_Stock."""

    # TODO: Define fields here
    qty = models.IntegerField("qty", null=False, blank=False)
    date = models.DateTimeField("date",auto_now_add=True)

    class Meta:
        """Meta definition for Stock."""
        abstract = True

    
class Product_Stock(Stock):
   
    """Model definition for Product_Stock."""

    # TODO: Define fields here
    
    cluster = models.ForeignKey(Cluster, verbose_name="cluster", on_delete=models.CASCADE,
                        related_name="product_stock_cluster")
    size_instance = models.ForeignKey(Size, verbose_name="size_instance", on_delete=models.CASCADE,
                        related_name="product_stock_size_instance",null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name="product", on_delete=models.CASCADE,
                        related_name="product_stock")

    class Meta:
        """Meta definition for Product_Stock."""

        verbose_name = 'Product Stock'
        verbose_name_plural = 'Product Stocks'
        

    def __str__(self):
        """Unicode representation of Product_Stock."""
        return f'{self.cluster} - {self.product} - ({self.qty})'
    