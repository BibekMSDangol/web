from django.urls import path
from django.urls import URLPattern
from guitar import views

urlpatterns=[
    path('guitarview',views.guitarview, name="guitarview"),
    path('guitaradd',views.guitaradd, name="guitaradd"),
    path('guitaredit/<int:id>',views.guitaredit, name="guitaredit"),
    path('guitarupdate/<int:id>',views.guitarupdate, name="guitarupdate"),
    path('guitardelete/<int:id>',views.guitardelete, name="guitardelete"),
]