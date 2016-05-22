from django.contrib.auth.forms import AuthenticationForm
from django import forms

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
        username = forms.CharField(label="Login", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'login'}))
        password = forms.CharField(label="Password", max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password','type':'password'}))
            
