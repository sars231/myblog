from django.shortcuts import render
from django.http import HttpResponse

def cover(request):
    return render(request,'cover.html')

def blog_home(request):
    return render(request,'blog_home.html')


# Create your views here.
