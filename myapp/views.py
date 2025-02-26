from django.shortcuts import render, redirect, get_object_or_404

from .models import Task # importing my Task model
from .forms import TaskForm  # Importing the TaskForm


# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello there World")

def task_list(request):
    tasks = Task.objects.all() # Getting all tasks from the database
    #print(tasks)  # Printing tasks to the console for debugging

    #return render(request, 'task_list.html', {'tasks':tasks})  # Passing tasks to the template
    return render(request, 'myapp/task_list.html', {'tasks': tasks})

#Create a Task 
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'myapp/add_task.html', {'form': form})

# Editing a task
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch task by ID or return 404
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'myapp/edit_task.html', {'form': form, 'task': task})

# Delete a task
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    return render(request, 'myapp/delete_task.html', {'task': task})
