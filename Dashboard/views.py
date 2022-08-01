from django.shortcuts import render, HttpResponse
from .models import Dashboard
# Create your views here.


def elearn(request):
    
    dboards = Dashboard.objects.all()
    
    return render(request, 'dashboard.html', {'dboards': dboards})
        

