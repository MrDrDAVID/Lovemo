from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request) :
    '''Lovemo user creation'''
    return render(request, 'register/register.html')