from django import forms
from django.forms import ModelForm
from .models import task

class TaskForm(ModelForm):
    
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task Title', 'class': 'w-full p-2 border rounded-md focus:ring-2 focus:ring-blue-500 outline-none'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Task Description', 'class': 'w-full p-2 border rounded-md mt-2 focus:ring-2 focus:ring-blue-500 outline-none'}))

    
    class Meta:
        model = task
        fields = "__all__"
        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'w-4 h-4 text-blue-600 border-gray-300 rounded'})
        }