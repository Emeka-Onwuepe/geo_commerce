from django.db.models.signals import pre_save, post_save, post_delete,m2m_changed
from django.dispatch import receiver
from Branch.models import (Cluster_Product,  Product_Size)
from Product.models import  Product

# products signals
@receiver(pre_save, sender=Product)
def update_Product_image(sender, instance, *args, **kwargs):
    if instance.pk:
        product = Product.objects.get(pk=instance.pk)
        if product.image != instance.image:
            product.image.delete(False)
            
    
@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, using, *args, **kwargs):
    if instance.image:
        instance.image.delete(save=False)  
        
def handle_cluster_product(instance,key):
    mapper = {'product':[Cluster_Product,Product_Size],
            #   'suit':[cluster_Suit,Suit_Size],
            #   'top':[cluster_Tops,Tops_Size],
            #   'foot_wear':[cluster_Foot_Wear,Foot_Wear_Size],
    
              }
    
    clusteres = cluster.objects.all()
    for cluster in clusteres:  
        cluster_product,created = mapper[key][0].objects.get_or_create(cluster = cluster,
                                                                      product = instance)
        
        if instance.sizes.exists():                                                          
            for size in instance.sizes.all():
                product_size,created_ = mapper[key][1].objects.get_or_create(cluster_instance = cluster_product,
                                                                             size = size)
        
                 
@receiver(post_save, sender=Product)
def product_saved(sender, instance,*args,**kwargs):
    handle_cluster_product(instance,'product')

@receiver(m2m_changed, sender=Product.sizes.through)
def product_sizes_changes(sender, instance,action,reverse,model,pk_set,**kwargs):
    if action == "post_add":
        handle_cluster_product(instance,'product')
        

        