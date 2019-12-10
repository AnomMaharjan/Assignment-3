from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time


# Create your views here.
def base(req):
    return HttpResponse("Hello! Welcome to Django bootcamp!")


def today(req):
  return HttpResponse("Today's date is: {}".format(datetime.date.today()))


def timestamp(req):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
