from django.shortcuts import render
from .models import Transactions, EarnLoviesOrBuy
# Create your views here.
def index(request) :
    '''The Lovemo homepage'''
    transactions = Transactions.objects.all()

    return render(request, 'main_app/index.html', {'transactions': transactions})

def transaction(request, id) :
    '''View for more detailed transaction'''
    transaction = Transactions.objects.get(id= id)
    comments = transaction.comments_set.all()

    return render(request, 'main_app/transaction.html', {'transaction':transaction, 'comments':comments})