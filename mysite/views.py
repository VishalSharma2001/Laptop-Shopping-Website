from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,'Home.html')
# def index(request):
#     return HttpResponse("This is Home Page")
def about(request):
    return HttpResponse("This is about Page")
    #return render(request,'about.html')
def contact(request):
    return HttpResponse("This is contact Page")
def tracker(request):
    return HttpResponse("This is tracker Page")
def search(request):
    return HttpResponse("This is search Page")
def productview(request):
    return HttpResponse("This is productview Page")
def checkout(request):
    return HttpResponse("This is checkout Page")