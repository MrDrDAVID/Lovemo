from django.db import models
from django.contrib.auth.models import User

EARN_OR_BUY = [('EARN', 'Earn'), ('BUY', 'Buy')]

# Create your models here.
class Lovies(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lovie_bank = models.IntegerField(default=1000)

class Boo(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boo = models.CharField(max_length=30)

class Transactions(models.Model) :
    payment_from = models.CharField(max_length=30, blank=False)
    payment_to = models.CharField(max_length=30, blank=False)
    payment_for = models.TextField(max_length=300)
    amount_payed = models.IntegerField(blank=False)
    date_of_transaction = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) :
        formatted_str = self.payment_from + ' paid ' + self.payment_to + ' {:,} lovies'.format(self.amount_payed)
        return formatted_str

    class Meta :
        db_table = 'Transactions'
        verbose_name = 'Transaction'

class Comments(models.Model) :
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    commentor = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    likes = models.IntegerField(default=0, null=True)

    def __str__(self):
        if len(self.description) > 100 :
            return self.description[:100] + '...'
        else :
            return self.description

    class Meta :
        verbose_name = 'Comment'
    

class EarnLoviesOrBuy(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    value = models.IntegerField(blank=False)
    earn_or_buy = models.CharField(max_length=4, choices=EARN_OR_BUY)
    completed = models.BooleanField()

    def __str__(self) :
        if len(self.description) > 20 :
            return self.description[:20] + '...'
        else :
            return self.description
    
    class Meta :
        db_table = 'Earn/Buy Lovies'
        verbose_name = 'Earn/Buy'