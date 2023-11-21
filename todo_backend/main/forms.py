from .models import ToDoTask
from django.forms import ModelForm, TextInput

class ToDoTaskForm(ModelForm):
    class Meta:
        model = ToDoTask
        fields = ['title', 'description']

        widgets = {
            "title" : TextInput(attrs={
                'placeholder': " Write some task..."
            }),
            "description": TextInput(attrs={
                'placeholder': " Write some description..."
            })

        }