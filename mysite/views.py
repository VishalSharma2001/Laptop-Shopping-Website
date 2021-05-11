from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Product
from math import ceil

# def index(request):
#     products=Product.objects.all()
#     n=len(products)
#     nSlides=n//4+ceil((n/4)+(n//4))
#     params={"no_of_Slides":nSlides,'range':range(1,nSlides),'product':products}
#     return render(request,'Home.html',params)

def index(request):
    products=Product.objects.all()
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        print("gasdhnadfnasfdfknbLNB;ksdgb",n)
        nSlides=n//4+ceil((n/4)+(n//4))
        allProds.append([prod,range(1,nSlides),nSlides]) 
    params={'allProds':allProds}
    return render(request,'Home.html',params)
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