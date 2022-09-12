from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models.task import Task

# Create your views here.

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"] # modificado para agregar email sino lo podemos sacar

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "stage"]
        widgets = {'stage': forms.HiddenInput()}