from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime


def index(request):
    now = datetime.datetime.now() - datetime.timedelta(hours=2)
    return render(request, 'index.html', {})


def about(request):
    now = datetime.datetime.now() - datetime.timedelta(hours=2)
    return render(request, 'about.html', {})



