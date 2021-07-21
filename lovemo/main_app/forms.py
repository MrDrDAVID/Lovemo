from django import forms

class SendLovies(forms.Form) :
    to = forms.CharField(max_length=30)
    amount = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea())

class NewComment(forms.Form) :
    comment = forms.CharField(label='New comment', widget=forms.Textarea())
