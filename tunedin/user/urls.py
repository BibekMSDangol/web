from django.urls import path
from user import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('adminview', views.adminview),
    path('addadmin', views.addadmin),
    path('editadmin/<int:id>', views.editadmin),
    path('updateadmin/<int:id>', views.updateadmin),
    path('deleteadmin/<int:id>', views.deleteadmin),
]