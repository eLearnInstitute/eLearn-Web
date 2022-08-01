from django.shortcuts import render, HttpResponse
from .models import Faculties

# Create your views here.

def home(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'preloader.html')
    
def others(request):
    return HttpResponse(request, 'other.html')
    
def faculties(request):    
    facultys = Faculties.objects.all()
    return render(request,'teacher.html', {'facultys': facultys})
    
    
    

