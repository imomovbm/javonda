from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, name):
    return HttpResponse(f"Assalomu aleykum,   {name}")

def bekzod(request):
    return HttpResponse("Assalom Bekzod")

def ruhshona(request):
    return HttpResponse("Assalom Rushi")
