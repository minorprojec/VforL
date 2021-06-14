from django.urls import path

from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('thirdpage',thirdpage, name='thirdpage'),
    path('secondpage',secondpage, name='secondpage'),
    path('grocerypage',grocerypage, name='grocerypage'),
    path('gurudevpage',gurudevpage, name='gurudevpage'),
    path('gauravpage',gauravpage, name='gauravpage'),
    path('fruitshop',fruitshop, name='fruitshop'),
    path('header',headerpage, name='headerpage'),
    path('footer',footerpage, name='footerpage'),
    path('add',add, name='add'),
    path('localshop/',localshop, name='localshop')
    
]