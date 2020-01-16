from django.shortcuts import render
from django.http import HttpResponse


def client(request):
    return HttpResponse('client')

def dashboard(request):
    return HttpResponse('dashboard')
