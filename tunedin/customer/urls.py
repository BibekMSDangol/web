from django.urls import path
from customer import views


urlpatterns = [
    path('', views.index),
    path('adminregister', views.register),
    path('adminlogin', views.login),
    path('homepage', views.homepage),
    path('addcustomer', views.addcustomer),
    path('customerview', views.customerview),
    path('editcustomer/<int:id>', views.editcustomer),
    path('updatecustomer/<int:id>', views.updatecustomer),
    path('deletecustomer/<int:id>', views.deletecustomer),
    path('acoustic',views.acoustic),
    path('all',views.all),
    path('electric',views.electric),
    path('electroacoustic',views.electroacoustic),
    path('bass',views.bass),
    
    
]