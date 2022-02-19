from unicodedata import name
from django.urls import path
from customer import views


urlpatterns = [
    path('', views.index, name="index"),
    path('adminregister', views.register, name="adminregister"),
    path('adminlogin', views.login, name="adminlogin"),
    path('homepage', views.homepage),
    path('addcustomer', views.addcustomer, name="addcustomer"),
    path('customerview', views.customerview, name="customerview"),
    path('editcustomer/<int:id>', views.editcustomer, name="editcustomer"),
    path('updatecustomer/<int:id>', views.updatecustomer, name="updatecustomer"),
    path('deletecustomer/<int:id>', views.deletecustomer, name="deletecustomer"),
    path('acoustic',views.acoustic),
    path('all',views.all),
    path('electric',views.electric),
    path('electroacoustic',views.electroacoustic),
    path('bass',views.bass),
    
    
]