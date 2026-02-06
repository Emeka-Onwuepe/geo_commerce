from django.db.models.signals import pre_delete,m2m_changed,post_save
from django.dispatch import receiver
from Branch.models import (Cluster_Product, Product_Size)
from Sales.models import Items, Sales


def manage_stock(instance,cluster,action='add'):
    mapper = {'product':[Cluster_Product,Product_Size],
            #   'suit':[cluster_Suit,Suit_Size],
            #   'top':[cluster_Tops,Tops_Size],
            #   'foot_wear':[cluster_Foot_Wear,Foot_Wear_Size],
              
              }
    
    model = instance.p_group
    
    if model == 'product':
        cluster_product,created = mapper[model][0].objects.get_or_create(cluster = cluster,
                                                                    product = instance.product)
        # product_size,created_ = mapper[model][1].objects.get_or_create(cluster_instance = cluster_product,
        #                                                                 size = instance.size_instance) 
    # elif model == 'suit':
    #     cluster_product,created = mapper[model][0].objects.get_or_create(cluster = cluster,
    #                                                                 product = instance.suit)
      
    product_size,created_ = mapper[model][1].objects.get_or_create(cluster_instance = cluster_product,
                                                                        size = instance.size_instance)
        
    if action == 'delete' or action == 'remove' :
        product_size.current_qty += instance.qty
        product_size.save()
        instance.delete()
        return
 
    product_size.current_qty -= instance.qty
    product_size.save()


@receiver(m2m_changed, sender= Sales.items.through)
def sales_multipleSIzes_changes(sender, instance,action,reverse,model,pk_set,**kwargs):
    if action == "post_add" and instance.paid and instance.channel == "store":
        for item_id in pk_set:
            item = Items.objects.get(pk=item_id)
            manage_stock(item,instance.cluster,action='add')
    elif action == 'pre_remove' and instance.paid:
        for item_id in pk_set:
            item = Items.objects.get(pk=item_id)
            manage_stock(item,instance.cluster,action='remove')
            
@receiver(post_save, sender=Sales)
def mark_as_paid(sender, instance, *args, **kwargs): 
    if instance.paid and instance.channel == "web":
        for item in instance.items.all():
            manage_stock(item,instance.cluster,action='add')
        
@receiver(pre_delete, sender=Sales)
def delete_sale(sender, instance, *args, **kwargs):
    for item in instance.items.all():
        manage_stock(item,instance.cluster,action='delete')