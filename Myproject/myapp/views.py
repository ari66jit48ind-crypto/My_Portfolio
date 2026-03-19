from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello, World!")
    #return render(request, 'home.html')
    return render (request ,'resume.html')