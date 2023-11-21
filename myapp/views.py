from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world!")


def show(request):
    return HttpResponse("show page")
# Create your views here.
