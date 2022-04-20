from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import ToDoForm
from app.models import Todos

# Create your views here.
def index(request):
    return render(request, 'index.html')


def todos(request):
    context={'tasks': Todos.objects.all() }
    return render(request, 'todos.html', context)

def add_todo(request):
    form = ToDoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'A new task have been created successfully')
        return redirect('todos')
    else:
        messages.error(request, 'Did not create the task')
    context={'form':form}
    return render(request, 'add_todo.html', context)