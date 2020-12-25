from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def detailes(request):
    return  HttpResponse('<h1> hello welcome to pytho web framewwork</h1>')
def second(request):
    return  HttpResponse('this git hub pratice framwowek')