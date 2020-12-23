import os

from django.http import HttpResponse
from django.shortcuts import render

from .models import Greeting


def index(request):
    return render(request, "index.html")


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()[:-10]
    return render(request, "db.html", {"greetings": greetings})
