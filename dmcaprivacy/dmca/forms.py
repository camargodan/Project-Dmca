from django import forms


class CompleteUser(forms.For):
    first_name = forms.CharField()
    last_name = forms.CharField()
