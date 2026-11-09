from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RoyxatdanOtishForm
# Create your views here.

def index(request, name):
    return HttpResponse(f"Assalomu aleykum,   {name}")

def bekzod(request):
    return HttpResponse("Assalom Bekzod")

def bekzod(request):
    return HttpResponse("Assalom Saydullo")

def ruhshona(request):
    return HttpResponse("Assalom Rushi")

def register(request):
    if request.method == "POST":
        form = RoyxatdanOtishForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz!")
            return redirect("register")
    else:
        form = RoyxatdanOtishForm()
    return render(request, "user/register.html", {"form": form})
