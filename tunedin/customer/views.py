from pprint import pprint
from django.http import request
from django.shortcuts import redirect, render
import customer
from customer.forms import CustomerForm
from customer.models import Customer
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from guitar.models import Guitar
# Create your views here.

def homepage(request):
    return render(request, 'customer/main.html')

def index(request):
    guitars = Guitar.objects.all()
    return render(request,"customer/index.html",{'guitars':guitars})

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            return redirect('/user/adminview')
        else:
            messages.error(request, "bad credentials")
            return redirect('/admin/adminlogin')
    return render(request, 'admin/l.html')

def register(request):
    if request.method=="POST":
        name=request.POST['name']
        username= request.POST['username']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        user = User.objects.create_user(first_name=name, last_name=phonenumber, email=email, username=username, password=password)
        user.save()
        return redirect('/adminlogin')
    return render(request, 'admin/r.html')

def customerview(request):
    print(request)
    customers=Customer.objects.raw('select * from customer')
    return render(request,"customer/view.html",{'customers':customers})

def addcustomer(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/customerview")
            except:
                print("Validation Failed")
    else:
        form=CustomerForm()
        print("invalid")
    return render(request,"customer/add.html", {'form':form})
    
def editcustomer(request,id):
    try:
        customer = Customer.objects.get(id=id)
        return render(request, 'customer/edit.html',{'customer':customer})
    except:
        print('no data found')
        return redirect('customerview')

def updatecustomer(request,id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(request.POST, instance=customer)
    if form.is_valid():
        try:
            form.save()
            return redirect('/customerview')
        except:
            print("Cannot Change")
    return render(request, 'customer/edit.html',{'customer':customer})

def deletecustomer(request, id):
    try:
        customer = Customer.objects.get(id=id)
        customer.delete()
    except:
        print("No data Found")
    return redirect("/customerview")
def all(request):
    guitars = Guitar.objects.all()
    return render(request, 'customer/index.html',{'guitars':guitars})

def acoustic(request):
    guitars = Guitar.objects.filter(guitar_type='Acoustic Guitar')
    return render(request,"customer/index.html",{'guitars':guitars})

def electric(request):
    guitars = Guitar.objects.filter(guitar_type='Electric Guitar')
    return render(request, 'customer/index.html', {'guitars':guitars})

def electroacoustic(request):
    guitars = Guitar.objects.filter(guitar_type='Electro-Acoustic Guitar')
    return render(request, 'customer/index.html', {'guitars':guitars})

def bass(request):
    guitars = Guitar.objects.filter(guitar_type='Bass Guitar')
    return render(request, 'customer/index.html', {'guitars':guitars})

