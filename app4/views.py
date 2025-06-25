from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def function(request):
    return HttpResponse("Welcome to my page")

from django.template import loader
def login(request):
    return render(request, 'index.html')