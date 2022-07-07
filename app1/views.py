from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.template.loader import render_to_string

# Create your views here.


def home(request):
    text=render_to_string("app1/Home")
    return HttpResponse(text)

def newDonor(request):
    text=render_to_string("app1/NewDonor")
    return HttpResponse(text)

def aboutUs(request):
    text=render_to_string("app1/About Us")
    return HttpResponse(text)

def contactUs(request):
    text=render_to_string("app1/Contact US")
    return HttpResponse(text)