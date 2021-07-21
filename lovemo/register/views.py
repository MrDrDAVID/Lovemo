from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request) :
    '''Lovemo user creation'''
    if request.method == 'POST' :
        reg_form = UserCreationForm(request.POST)

        if reg_form.is_valid() :
            reg_form.save()
    else :
        reg_form = UserCreationForm()

    return render(request, 'register/register.html', {'form': reg_form})