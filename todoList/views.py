import datetime

from .models import Todo
from .forms import TaskForm
from django.shortcuts import render, redirect

# The index view is where tasks are viewed or searched for
def index(request):
    search_term = request.GET.get('search') or ''
    return render(request, 'todoList/index.html', context={
        'tasks': Todo.objects.filter(task_name__contains=search_term).all(),
        'previous_search': search_term,
    })

# The add view is where new tasks are born
def add(request):
    # Unless a completed form is being POSTed to the server, simply return the add page
    if(request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    context = {'form': TaskForm()}
    return render(request, 'todoList/add.html', context)

# The update view is where old tasks are updated
def update(request, id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task.edited_at = datetime.datetime.utcnow()
        form.save()
        return redirect('../../')
    return render(request, 'todoList/update.html', {'form': form})

# The delete view is where the eldest tasks are put to rest
def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('../../')