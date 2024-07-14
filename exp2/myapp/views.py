from django.http import HttpResponse
from django.shortcuts import render
import datetime


# Create your views here.
def aheadtime(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=4)
    resp="<h1>Current date and Time ahead by 4 hrs is %s </h1>"%(dt)
    return HttpResponse(resp)

def beforetime(request):
    dt=datetime.datetime.now()+datetime.timedelta(hours=-4)
    resp="<h1>Current Server Date and Time Before 4hrs is %s</h1>"%(dt)
    return HttpResponse(resp)