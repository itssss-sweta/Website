from django.shortcuts import render,HttpResponse
from datetime import datetime
from myApp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        "variable":"done"
    }
    return render(request,'project.html',context)
    #return HttpResponse('Hello World')

def about(request):
    return render(request,'about.html')
    #return HttpResponse('Why bother buying,when you can rent!')

def service(request):
    return render(request,'service.html')

    #return HttpResponse('Services not updated')

def signin(request):
    return render(request,'signin.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request,'contact.html')
