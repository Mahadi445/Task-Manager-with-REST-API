from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete', 'photo']
    


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
