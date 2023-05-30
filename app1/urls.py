from django.urls import path
from app1.views import *

urlpatterns = [
    path('all/',demo_all),
    path('filter/',demo_filter),
    path('get/',demo_get),
    path('login/',login,name='login'),
    path('logout/',logout,name="logout"),
    path('',index,name="index"),
    path('product-all/',productall,name='productall'),
    path('product-filter/<int:id>',product_categorywise,name='productcat'),
    path('product-get/<int:id>',product_get,name='productget'),
    path('register/',register,name='register')
    


]