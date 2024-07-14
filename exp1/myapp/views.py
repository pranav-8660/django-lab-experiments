from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def current_dateandtime(request):
    dt = datetime.datetime.now()
    responsE = "<h1>current date and time is %s<h1>"%dt
    return HttpResponse(responsE)
