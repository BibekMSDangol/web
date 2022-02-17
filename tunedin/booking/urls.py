from django.urls import path
from booking import views
from customer import urls

urlpatterns=[
    path('bookingview',views.bookingview),
    path('bookingadd',views.bookingadd),
    path('bookingdelete/<int:id>',views.bookingdelete)
]