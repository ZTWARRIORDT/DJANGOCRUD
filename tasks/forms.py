from django.forms import ModelForm
from .models import Tasks
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }