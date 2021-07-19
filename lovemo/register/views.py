from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def register(request) :
    return render(request, 'templates/register/register.html')