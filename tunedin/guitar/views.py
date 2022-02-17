from django.shortcuts import render, redirect
from guitar.forms import GuitarForm
from guitar.models import Guitar

# Create your views here.
def guitarview(request):
    guitars= Guitar.objects.all()
    return render(request,'guitar/view.html',{'guitars':guitars})
def guitaradd(request):
    if request.method == "POST":
        form = GuitarForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/guitar/guitarview")
            except:
                print("Failed")
    else:
        form = GuitarForm()
        print("invalid")
    return render (request,'guitar/add.html',{'form':form})

def guitaredit(request,id):
    try:
        guitar = Guitar.objects.get(id=id)
        return render(request, "guitar/edit.html", {'guitar': guitar})
    except:
        print("No data found")
    return redirect("guitar/guitarview")

def guitarupdate(request,id):
    guitar = Guitar.objects.get(id=id)
    form = GuitarForm(request.POST, instance=guitar)
    if form.is_valid():
        try:
            form.save()
            return redirect("/guitar/guitarview")
        except:
            print("Validation Failed")
    return render(request, "guitar/edit.html", {'guitar':guitar})

def guitardelete(request,id):
    try:
        guitar = Guitar.objects.get(id=id)
        guitar.delete()
    except:
        print("cannot perform")
    return redirect("/guitar/guitarview")
