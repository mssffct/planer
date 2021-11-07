from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateInput, TimeInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'task_title', 'task_text',
            'task_date', 'start_time', 'end_time'
        ]
        widgets = {
            'task_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название задачи'
            }),
            'task_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Детали'
            }),
            'task_date': DateInput(attrs={
                'type': 'date',
                'id': 'task_date'
            }),
            'start_time': TimeInput(attrs={
                'type': 'time',
                'id': 'start_time'
            }),
            'end_time': TimeInput(attrs={
                'type': 'time',
                'id': 'end_time'
            }),
        }
