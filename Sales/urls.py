from rest_framework import routers
from django.urls import path

from .import views
router = routers.DefaultRouter()


app_name="sales"

urlpatterns = [ 
    path('',views.salesView,name="salesView"), 
    path('process',views.processSalesView,name="processSalesView"),
    path('<int:productTypeId>/<str:pgroup>/<str:brand>',views.salesProductView,name="salesProductView"),
    path('sale/<str:purchaseId>/<str:type>',views.saleView,name="saleView"), 
    path('analysis/<int:clusterID>/<str:date>/',views.salesAnalysisView,name="salesAnalysisView"),
    path('<str:start_date>/<str:end_date>/<int:clusterID>/rangeanalysis',views.rangeSalesView,name="rangeSalesView"),

]
urlpatterns += router.urls