from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from main_app.models import Boo, Lovies

# Create your views here.
def register(request) :
    '''Lovemo user creation'''
    if request.method == 'POST' :
        reg_form = RegisterForm(request.POST)

        if reg_form.is_valid() :
            new_boo = reg_form.cleaned_data['boo']

            new_user = reg_form.save()
            new_user.save()

            boo = Boo()
            boo.user = new_user
            new_user.boo.boo = new_boo
            boo.save()

            bank = Lovies()
            bank.user = new_user
            new_user.lovies.save()

            return HttpResponseRedirect('/home')

    else :
        reg_form = RegisterForm()

    return render(request, 'register/register.html', {'form': reg_form})