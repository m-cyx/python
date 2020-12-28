from django import forms
from .models import Task
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = TaskForm
        fields = ["title", "task"]
        