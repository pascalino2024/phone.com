from django.urls import path
from.import views

urlpatterns = [
   
    path("aboutus",views.aboutus),
    path("contact",views.contact),
    path("login",views.login),
    path("register",views.register),
    path("whishlist",views.wishlist),
    path("compare",views.compare),
    path("index",views.index),
    

    path("",views.index),
    #ici <model> est un paramètre represant le brand
    path("<brands>",views.brands)
] 