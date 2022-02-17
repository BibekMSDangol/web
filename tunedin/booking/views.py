from django.shortcuts import render, redirect
from booking.forms import BookingForm
from booking.models import Booking
# Create your views here.

def bookingview(request):
    bookings= Booking.objects.all()
    return render(request, 'booking/view.html', {'bookings':bookings})

def bookingadd(request):
    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/booking/bookingview")
            except:
                print("Failed")
    else:
        form = BookingForm()
        print("invalid")
    return render (request,'booking/add.html',{'form':form})   

def bookingdelete(request,id):
    try:
        booking = Booking.objects.get(id=id)
        booking.delete()
    except:
        print("cannot perform")
    return redirect("/booking/bookingview")