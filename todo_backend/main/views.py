from django.shortcuts import render, redirect
from .models import ToDoTask
from .forms import ToDoTaskForm
# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def index(request):
    error = ''
    if request.method == 'POST':
        form = ToDoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todopage')
        else:
            error = 'NO CORRECT TASK'

    form = ToDoTaskForm()

    data = {
        'form' : form,
        'error': error,
    }

    return render(request, 'main/todo_list.html', data)