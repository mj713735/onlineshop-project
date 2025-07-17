from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context ={
        "is_admin":True,
        "user":["amir","mohammad","ali"]
        
    }
    return render(request,"index.html",context) 