from typing import Any
from django.db import models

# Create your models here.

class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField("Category",max_length = 150,null=False,blank=False)
    image = models.ImageField(verbose_name="image", default="suits2.jpg",null=True,blank=True)
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def name_slug(self):
        return self.name.replace(' ','_')

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Product_Type(models.Model):
    """Model definition for Product_Type."""
    
    # SUITS = 'suits'
    # FOOT_WEAR = 'foot_wear'
    # TOP = 'top'
    PRODUCT = 'product'

    P_GROUP = [
            #     (SUITS,SUITS),
            #    (FOOT_WEAR,FOOT_WEAR),
            #    (TOP,TOP),
               (PRODUCT ,PRODUCT)
                ]

    # TODO: Define fields here
    name = models.CharField("name",max_length = 200,null=False,blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="category")
    p_group = models.CharField(
        max_length=10,
        choices=P_GROUP,
        default=PRODUCT,
    )
    
    
    
    class Meta:
        """Meta definition for Product_Type."""

        verbose_name = 'Product_Type'
        verbose_name_plural = 'Product_Types'

    def __str__(self):
        """Unicode representation of Product_Type."""
        return f"{self.category} - {self.name}"


class Size(models.Model):
    """Model definition for Size."""
    
   
    
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE,related_name="size_product_type")
    size = models.CharField(verbose_name="size", max_length=150)
    price = models.IntegerField(verbose_name="price")
   

    class Meta:
        """Meta definition for Size."""

        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        """Unicode representation of Topping."""
        return f' {self.product_type}-{self.size}-{self.price}'
    
    
class Product_Abstract(models.Model):
    """Model definition for Product."""
    
    # TODO: Define fields here
    type = models.CharField(verbose_name="type",default=None, max_length=60,null=True,blank=True)
    brand = models.CharField(verbose_name="brand",default=None, max_length=60,null=True,blank=True)
    date = models.DateField("date", auto_now=False, auto_now_add=True)
    publish = models.BooleanField(default=False)
    
    class Meta:
        """Meta definition for Product."""
        abstract = True
        

    
class Product(Product_Abstract):
    product_type = models.ForeignKey(Product_Type, on_delete=models.CASCADE, related_name="product_type")
    image = models.ImageField(verbose_name="image", default="trousers.jpg",null=True,blank=True)
    sizes = models.ManyToManyField(
        Size, verbose_name="sizes", related_name="product_sizes", blank=True)
    
    def get_meta(self):
        meta = {}
        for key,value in self.__dict__.items():
            if key not in ['image','_state','publish',
                           'date']:
                meta[key] = value
        return meta

    
    def name(self):
        exclude = [None, 'None','none','Normal','normal'] 
        if self.brand not in exclude:
            return f'{self.brand} {self.product_type.category.name}'
        else:
            return f'{self.product_type.name} {self.product_type.category.name}'
    
    def get_details(self):
        details = ''
        data = self.__dict__
        exclude = ['id','product_type' ,'sizes','description',
                   'publish','brand','color','date',
                   'product_type_id','_state','image',
                   'type'
                   ]
        
        for key,value in data.items():
            if key not in exclude:
                if not value or value.lower() in ['adult','no','none','normal','male','single']:
                    continue
                
                details += f'{key.lower()} : {value},  '
        return details[0:-3]
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-date','product_type']
        # abstract = True

    def __str__(self):
        """Unicode representation of Product."""
        return f"{self.product_type}"