from django.shortcuts import render, HttpResponse
from .models import Course

# Create your views here.


def course(request):     
    crses = Course.objects.all()
    return render(request,'courses.html', {'crses': crses})
    
