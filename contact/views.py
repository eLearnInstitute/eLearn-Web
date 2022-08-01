from django.shortcuts import render, HttpResponse
from contact.models import Contact
from django.contrib import messages

# Create your views here.


def contact(request):
    messages.success(request, 'Welcome to Contact')
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        ph_num = request.POST['ph_num']
        message = request.POST['message']
        description = request.POST['description']
        contact = Contact(name=name, email=email, ph_num=ph_num, message=message, description=description)
    return render(request, 'contact.html')

