from django.urls import path
from . import views # . means this directory and give access to views file

urlpatterns = [
 # create a webpage and then need to modify this APPS URL file
 path('',views.home,name="home") # views.py and call home function
 , path ('about.html',views.about,name="about"),
 path ('stocks.html',views.stocks,name="stocks"),
 path ('delete/<stock_id>',views.delete,name="delete"),
 path ('delete_stock.html',views.delete_stock,name="delete_stock"),
]