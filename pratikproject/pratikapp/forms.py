from django import forms
from django.contrib.auth.models import User
from pratikapp.models import Task

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username",'email','password']


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        
