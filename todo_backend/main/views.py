from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy

from .models import ToDoTask
from .forms import ToDoTaskForm
from django.views.generic import DeleteView
# Create your views here.

def main(request):
    return render(request, 'main/main.html')
class DeleteTask(DeleteView):
    model = ToDoTask
    template_name = 'main/confirm_delete.html'
    success_url = reverse_lazy('todopage')

    def get_object(self, queryset=None):
        return ToDoTask.objects.get(pk=self.kwargs['pk'])
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
    tasks = ToDoTask.objects.all()

    data = {
        'form' : form,
        'error': error,
        'tasks': tasks,
    }

    return render(request, 'main/todo_list.html', data)

