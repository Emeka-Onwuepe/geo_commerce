from django.urls import path,include

from frontend.views import home, location

app_name = 'frontend'

urlpatterns = [
    path('',home,name='home'),
    path('location/', location, name='location'),
]
