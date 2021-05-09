from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def meni(request):
    return render(request, 'meni.html')    
# Create your views here.
def onama(request):
    return render(request, 'onama.html')

def kontakt(request):
    return render(request, 'kontakt.html')    