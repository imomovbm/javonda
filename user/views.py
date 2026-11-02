from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, name):
    return HttpResponse(f"Assalomu aleykum, {name}")

def ruhshona(request):
    return HttpResponse("Assalom Rushi")