from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def sayHello(request):
    return HttpResponse("Hello World")

def home(request):
    return render(request, 'index.html', {
        'current_year': datetime.now().year
    })
