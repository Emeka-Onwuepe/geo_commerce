from rest_framework import routers
from knox import views as KnoxView
from django.urls import path
from .import views
router = routers.DefaultRouter()


app_name="cluster"

urlpatterns = [
    
    path('<int:clusterId>/<str:action>',views.clusterView,name="clusterView"), 
 
]
urlpatterns += router.urls