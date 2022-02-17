from django.urls import path
from django.urls import URLPattern
from guitar import views

urlpatterns=[
    path('guitarview',views.guitarview),
    path('guitaradd',views.guitaradd),
    path('guitaredit/<int:id>',views.guitaredit),
    path('guitarupdate/<int:id>',views.guitarupdate),
    path('guitardelete/<int:id>',views.guitardelete),
]