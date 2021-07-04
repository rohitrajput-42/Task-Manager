from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Todo

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'password1': forms.TextInput(attrs = {'class': 'form-control'}),
            'password2': forms.TextInput(attrs = {'class': 'form-control'}),
        }

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status']

        widget = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'status': forms.TextInput(attrs = {'class': 'form-control'})
        }