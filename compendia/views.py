from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *

#class DoctorListView(ListView):
#    model=Doctor

#    def show(self):
    

def index(request):
    return HttpResponse("Hi, finally!")
# Create your views here.

#def
