from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string 
# Create your views here.

               
marque = {  "Apple" : "Apple",
            "Blackberry":"Blackberry",
            "HTC":"HTC",
            "Oppo":"Oppo",
            "Nokia":"Nokia",
            "Samsung":"Samsung",
            "Infinix" : "Infinix",
            "Itel" : "Itel",
            "Huawei": "Huawei",
            "Tecno":"Tecno",
            "Pixel" :"Pixel",
            "Others": "Others"}

def aboutus(request):
    return render(request,"challenges/aboutus.html")


def contact(request):
    return render(request,"challenges/contact.html")

def login(request):
    return render(request,"challenges/login.html")

def register(request):
    return render(request,"challenges/register.html")

def wishlist(request):
    return render(request,"challenges/wishlist.html")

def compare(request):
    return render(request,"challenges/compare.html")


def brands(request,brands):
  # this function is here to the brands selevted
    try:
        themarques =  marque[brands]
        return render(request,"challenges/product-models.html",{
            "brands":themarques.capitalize()
        })
    except:
         return HttpResponseNotFound("<h1> Page not Found </h1>")
       

   


def index(request):
    try:
          # in this case the key is the fisrt january before : 
        brandslist = list(marque.keys())
        return render(request,"challenges/index.html",{
            "brandslist":brandslist
        })
       
    except:
        return HttpResponseNotFound("<h1> Page not Found here </h1>")

 #def month_challenge(request ,month):
 #   return HttpResponse(month)