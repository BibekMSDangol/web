from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import user

from user.forms import UserForm

def dashboard(request):
    return render(request, 'admin/tdash.html')

def adminview(request):
    user = User.objects.all()
    return render(request, 'admin/view.html',{'users':user})

def addadmin(request):
    if request.method=="POST":
        name=request.POST['name']
        username= request.POST['username']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        user = User.objects.create_user(first_name=name, last_name=phonenumber, email=email, username=username, password=password)
        user.save()
        return redirect('/user/adminview')
    return render(request, 'admin/add.html')

def editadmin(request,id):
        user = User.objects.get(id=id)
        return render(request, 'admin/edit.html',{'user':user})
        


def updateadmin(request,id):
    user = User.objects.get(id=id)
    form=UserForm(request.POST, instance=user)
    if form.is_valid():
        try:
            form.save()
            return redirect('/user/adminview')
        except:
            print("Cant update")
    return render(request, 'admin/edit.html', {'user':user})

def deleteadmin(request,id):
    try:
        user=User.objects.get(id=id)
        user.delete()
    except:
        print("No data found")
    return redirect('/user/adminview')