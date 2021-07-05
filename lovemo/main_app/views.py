from django.shortcuts import render
from .models import Transactions, EarnLoviesOrBuy, Boo
from .forms import SendLovies

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

    return render(request, 'main_app/transaction.html', {'transaction':transaction, 'comments':comments})

def create_transaction(request) :
    '''Creating a new transaction'''
    lovie_form = SendLovies()

    return render(request, 'main_app/create_transaction.html', {'form': lovie_form})