from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Shaxi alfons")

def shahzod(request, ism):
    return HttpResponse(f"{ism} xush kelibsiz")