from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey there, here is the Rango App developed by Siddhesh <br /><a href = '/rango/about/'> About </a>")


def about(request):
    return HttpResponse("Here is the about page. <br /><a href = '/rango/'> Index </a>")

