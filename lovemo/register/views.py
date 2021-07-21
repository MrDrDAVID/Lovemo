from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm

# Create your views here.
def register(request) :
    '''Lovemo user creation'''
    if request.method == 'POST' :
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid() :
            reg_form.save()
    else :
        reg_form = RegisterForm()

    return render(request, 'register/register.html', {'form': reg_form})