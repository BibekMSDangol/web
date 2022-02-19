from django.urls import path
from user import views

urlpatterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('adminview', views.adminview, name="adminview"),
    path('addadmin', views.addadmin, name="addadmin"),
    path('editadmin/<int:id>', views.editadmin, name="editadmin"),
    path('updateadmin/<int:id>', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:id>', views.deleteadmin, name="deleteadmin"),
]