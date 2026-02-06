
from django.contrib import admin

from Branch.models import (Cluster, Cluster_Product, Product_Size)

# Register your models here.

admin.site.register(Cluster)
admin.site.register(Cluster_Product)
admin.site.register(Product_Size)
