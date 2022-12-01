from django import forms
from .models import Todo

# This form is specifically for receiving a new task.
class TaskForm(forms.ModelForm):
    task_name = forms.CharField(min_length=1, max_length=200, label='Task name')
    class Meta:
        model = Todo
        fields = ['task_name']