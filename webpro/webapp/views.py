from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#creat your views here.

from .models import Contact

from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        password = request.POST.get('password')
        address = request.POST.get('address')
        contact = Contact(name=name, address=address, email=email, password=password, contact=contact_no)
        messages.success(request,"your message sent succesfully.")
        contact.save()
    return render(request, 'contact.html')

def about(request):
    if request.method=="GET":
         output=request.GET.get('output')
    return render(request, 'about.html',{'output':output})

def training(request):
    return render(request, 'training.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def accountsetting(request):
    return render(request, 'accountsetting.html')


def userForm(request):
    finalans = 0
    data = {}  # Initialize an empty dictionary for data

    try:
        if request.method == 'POST':
            # Get values from the form and convert them to integers
            n1 = int(request.POST.get('num1', 0))  # Default to 0 if num1 is not provided
            n2 = int(request.POST.get('num2', 0))  # Default to 0 if num2 is not provided

            # Perform addition
            finalans = n1 + n2

            # Update data dictionary with input values and result
            data = {
                'n1': n1,
                'n2': n2,
                'output': finalans
            }
            url="/about/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except ValueError:  # Handle case where inputs are not integers
        data['error'] = "Please enter valid numbers."

    # Render the template with the data
    return render(request, "userform.html", data)
