from django.db import models
from Branch.models import Cluster

from Product.models import Product, Size

# Create your models here.
class Bad_Product_Abstract(models.Model):
    """Model definition for Bad_Product_Abstract."""

    # TODO: Define fields here
    qty = models.IntegerField("qty",null=False,blank=False)
    date = models.DateField("date", auto_now=False, auto_now_add=True)

    class Meta:
        """Meta definition for Bad_Product_Abstract."""
        abstract = True


class Bad_Product(Bad_Product_Abstract):
    """Model definition for Bad_Product."""

    # TODO: Define fields here
    product = models.ForeignKey(Product,verbose_name='product', on_delete=models.CASCADE,related_name = "bad_product_product_type")
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE, related_name="bad_product_cluster")
    size_instance = models.ForeignKey(Size, verbose_name="size_instance", on_delete=models.CASCADE,
                        related_name="bad_product_size_instance",null=True, blank=True)
    
    
    class Meta:
        """Meta definition for Bad_Product."""

        verbose_name = 'Bad_Product'
        verbose_name_plural = 'Bad_Products'
        ordering = ['-date']

    def __str__(self):
        """Unicode representation of Bad_Product."""
        return f'{self.cluster} - {self.product} ({self.date})'