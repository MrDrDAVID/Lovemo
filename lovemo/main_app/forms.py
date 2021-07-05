from django import forms

class SendLovies(forms.Form) :
    payment_to = forms.CharField(label='to', max_length=30)
    amount_paid = forms.IntegerField(label='amount')
    payment_for = forms.CharField(label='for', widget=forms.Textarea())
