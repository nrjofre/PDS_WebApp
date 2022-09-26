from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models.task import Task
from main.models.tarea import Tarea
from main.models.profile import Profile

# Create your views here.

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(label="Teacher", required=False)
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "is_staff"]

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "stage"]
        widgets = {'stage': forms.HiddenInput()}

class CreateTaskForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ["name", "statement", "image", "starting_stage", "difficulty"]
        widgets = {}