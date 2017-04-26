from django import forms
from .models import *

class TuiterForm(forms.ModelForm):
    class Meta:
        model = Tuiter
        fields = ('username', 'screenname', 'email', 'birthday', 'location', 'biography', 'customLink')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=16, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    screenName = forms.CharField(max_length=36, required=True, label="Name")
    email = forms.EmailField(required=True)
    birthday = forms.DateField(widget=forms.DateInput(), required=True)
    location = forms.CharField(max_length=36, required=True)
    biography = forms.CharField(max_length=256, required=True, label="Short description")
    customLink = forms.URLField(widget=forms.URLInput(), required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('content',)

class PerfilForm(forms.Form):
    nome = forms.CharField(max_length=36,required=True)
    biografia = forms.CharField(widget=forms.Textarea,required=False)
    local = forms.CharField(max_length=36,required=False)
    link = forms.URLField(required=False)