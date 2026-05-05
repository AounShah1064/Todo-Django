from django import forms
from django.forms import ModelForm
from .models import task

class TaskForm(ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task Description'}))

    
    class Meta:
        model = task
        fields = "__all__"