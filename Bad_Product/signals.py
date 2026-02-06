from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from Branch.models import  Cluster_Product,Product_Size
from Bad_Product.models import  Bad_Product


def manage_stock(instance,model,action='add'):
    mapper = {'product':[Cluster_Product,Product_Size,Bad_Product],
            #   'suit':[cluster_Suit,Suit_Size,Bad_Suit],
            #   'top':[cluster_Tops,Tops_Size,Bad_Top],
            #   'foot_wear':[cluster_Foot_Wear,Foot_Wear_Size,Bad_Foot_Wear],
              }
    
    cluster_product,created = mapper[model][0].objects.get_or_create(cluster = instance.cluster,
                                                                    product = instance.product)
    product_size,created_ = mapper[model][1].objects.get_or_create(cluster_instance = cluster_product,
                                                                        size = instance.size_instance) 
    
    if action == 'delete':
        product_size.bad_qty -= instance.qty
        product_size.current_qty += instance.qty
        product_size.save()
        return
    
    if instance.pk:
        old_instance = mapper[model][2].objects.get(pk=instance.pk)
        diff = instance.qty - old_instance.qty
        product_size.bad_qty += diff
        product_size.current_qty -= diff
        product_size.save()
    else:  
        product_size.bad_qty += instance.qty
        product_size.current_qty -= instance.qty
        product_size.save()

@receiver(pre_save, sender=Bad_Product)
def stock_added(sender, instance, *args, **kwargs):
    manage_stock(instance,'product')

@receiver(post_delete, sender=Bad_Product)
def stock_deleted(sender, instance, *args, **kwargs): 
    manage_stock(instance,'product','delete')
    
