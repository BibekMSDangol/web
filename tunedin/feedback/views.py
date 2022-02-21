from email import message
from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from feedback.models import Feedback

def feedbackview(request):
    print(request)
    feedback=Feedback.objects.raw('select * from feedback')
    return render(request,"customer/feedbackview.html",{'feedback':feedback})

def feedbackadd(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/")
            except:
                print("Validation failed")
    else:
        form=FeedbackForm()
        print("invalid")
    return render(request, "customer/feedback.html",{'form':form})
    
def feedbackdelete(request, id):
    try:
        feedback = Feedback.objects.get(id=id)
        feedback.delete()
    except:
        print("No data Found")
    return redirect("/feedback/feedbackview")