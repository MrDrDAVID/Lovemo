from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Transactions, EarnLoviesOrBuy, Boo, Comments
from .forms import SendLovies, NewComment

# Create your views here.
def index(request) :
    '''The Lovemo homepage'''
    transactions = Transactions.objects.all()

    return render(request, 'main_app/index.html', {'transactions': transactions})

def about(request) :
    '''The about page'''
    return render(request, 'main_app/about.html')

def transaction(request, id) :
    '''View for more detailed transaction'''
    transaction = Transactions.objects.get(id=id)
    comments = transaction.comments_set.all()

    if request.method == 'POST' :
        new_comment = NewComment(request.POST)

        if new_comment.is_valid() :
            comment = new_comment.cleaned_data['comment']
            transaction.comments_set.create(transaction=transaction, commentor='boo', description=comment)
            transaction.save()

            return HttpResponseRedirect('/%i' %transaction.id)

    else :
        new_comment = NewComment()

    return render(request, 'main_app/transaction.html', {'transaction':transaction, 'comments':comments, 'form':new_comment})

def create_transaction(request) :
    '''Creating a new transaction'''
    if request.method == 'POST' :
        lovie_form = SendLovies(request.POST)

        if lovie_form.is_valid() :
            pay_to = lovie_form.cleaned_data['payment_to']
            amount = lovie_form.cleaned_data['amount_paid']
            pay_for = lovie_form.cleaned_data['payment_for']
            new_transaction = Transactions(payment_from='you', payment_to=pay_to, payment_for=pay_for, amount_payed=amount)
            new_transaction.save()

            return HttpResponseRedirect('/home')
    else :
        lovie_form = SendLovies()

    return render(request, 'main_app/create_transaction.html', {'form': lovie_form})