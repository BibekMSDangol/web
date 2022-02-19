from unicodedata import name
from django.urls import path
from booking import views
from customer import urls

urlpatterns=[
    path('bookingview',views.bookingview, name="bookingview"),
    path('bookingadd',views.bookingadd, name="bookingadd"),
    path('bookingdelete/<int:id>',views.bookingdelete, name="bookingdelete")
]