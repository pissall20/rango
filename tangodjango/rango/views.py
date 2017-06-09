from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey there, here is the Rango App developed by Siddhesh")
