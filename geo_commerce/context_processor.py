
from Branch.models import Cluster
from Product.models import Category, Product, Product_Type

def context_processor(request):
    clusteres = Cluster.objects.all()
    categories = Category.objects.all()
    
    unsorted_categories = []
    # get published categories
    products = Category.objects.filter(category__product_type__publish = True)
    if products:
        unsorted_categories.append(products)
    # filter categories
    sorted_categories = []
    
    for pgroups in unsorted_categories:
        for category in pgroups:
            if category not in sorted_categories:
                sorted_categories.append(category)
                
    p_groups = []
    for group in Product_Type.P_GROUP:
        p_groups.append(group[0])
    
    return {"clusteres": clusteres, "categories":categories,
            "sorted_categories":sorted_categories,
            'product_groups':p_groups,}