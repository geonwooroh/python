from django.shortcuts import render
from .models import Post

def landing(request):
    return render(request,'single_page/landing.html')

def about_me(request):
    return render(request,'single_page/about_me.html')

