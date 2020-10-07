from django import forms
from django.contrib.auth.models import User
from . import models
class singininfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField(max_length=8)
    class Meta():
        model = User
        fields = ('username','password','email')
class loginform(forms.Form):
    username=forms.CharField(max_length=155)
    password=forms.CharField(max_length=155,widget=forms.PasswordInput())
