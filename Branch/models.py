from django.db import models

# Create your models here.

class Cluster(models.Model):
    """Model definition for cluster."""

    # TODO: Define fields here
    name = models.CharField('cluster Name', max_length = 200)

    class Meta:
        """Meta definition for cluster."""

        verbose_name = 'cluster'
        verbose_name_plural = 'clusteres'

    def __str__(self):
        """Unicode representation of cluster."""
        return self.name


class Cluster_Product(models.Model):
    """Model definition for cluster_Product."""

    # TODO: Define fields here
    cluster = models.ForeignKey(Cluster, verbose_name="cluster", 
                on_delete=models.CASCADE, related_name="cluster_product_cluster")  
    product = models.ForeignKey("Product.Product", verbose_name="product", 
                on_delete=models.CASCADE, related_name="cluster_product_product") 
  
  
    class Meta:
        """Meta definition for cluster_Product."""

        verbose_name = 'cluster_Product'
        verbose_name_plural = 'cluster_Products'

    def __str__(self):
        """Unicode representation of cluster_Product."""
        return f'{self.cluster} - {self.product}'
    

class Product_Size(models.Model):
    """Model definition for product_Size."""

    # TODO: Define fields here
    cluster_instance = models.ForeignKey(Cluster_Product, verbose_name="cluster_product",
                                       related_name = 'cluster_product_size',
                                       on_delete=models.CASCADE)
    size = models.ForeignKey("Product.Size", related_name='cluster_product_sizes',
                             on_delete=models.CASCADE)
    current_qty = models.IntegerField("current_qty", default=0)
    returned_qty = models.IntegerField("returned_qty", default=0)
    bad_qty = models.IntegerField("bad_qty", default=0)

    class Meta:
        """Meta definition for product_Size."""

        verbose_name = 'product_Size'
        verbose_name_plural = 'product_Sizes'

    def __str__(self):
        """Unicode representation of product_Size."""
        return f'{self.cluster_instance} - {self.size}'
