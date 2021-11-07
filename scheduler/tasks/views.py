from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def main(request):
    tasks = Task.objects.order_by('task_date')
    return render(request, 'tasks/main.html', {'title': 'Главная', 'tasks': tasks})


def view_all_tasks(request):
    tasks = Task.objects.order_by('task_date')
    return render(request, 'tasks/view_all.html', {'title': 'Все задачи', 'tasks': tasks})


def add_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('new_one')
        else:
            error = 'Заполните все поля'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'tasks/add_task.html', context)


def view_all_notes(request):
    return render(request, 'tasks/notes.html')


def new_one(request):
    return render(request, 'tasks/new_one.html')
