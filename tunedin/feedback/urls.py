from unicodedata import name
from django.urls import path
from feedback import views


urlpatterns=[
    path('feedbackview',views.feedbackview, name="feedbackview"),
    path('feedbackadd',views.feedbackadd, name="feedbackadd"),
    path('feedbackdelete/<int:id>', views.feedbackdelete, name="feedbackdelete")
]