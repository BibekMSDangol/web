from urllib import request
from django import forms
from booking.models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"
