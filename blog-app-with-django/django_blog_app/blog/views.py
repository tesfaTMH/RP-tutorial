from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to Blog app home page.</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to Blog app about page</h1>')