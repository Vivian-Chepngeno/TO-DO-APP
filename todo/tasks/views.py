from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()  # Retrieve all tasks from the database
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the list page after saving

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)  # Render the task list template

def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)  # Get the task or raise 404 if it doesn't exist
    form = TaskForm(instance=task)  # Pre-fill the form with the task's current data

    if request.method == 'POST':  # When form is submitted
        form = TaskForm(request.POST, instance=task)  # Bind form to the task instance
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('/')  # Redirect to the task list page

    context = {'form': form}  # Pass the form to the template
    return render(request, 'tasks/update.html', context)  # Render the update template

def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk)  # Get the task or raise a 404 error if it doesn't exist
    if request.method == 'POST':  # Check if the request method is POST (for deletion confirmation)
        item.delete()  # Delete the task
        return redirect('/')  # Redirect to the task list page after deletion

    context = {'item': item}  # Pass the item to the template
    return render(request, 'tasks/delete.html', context)  # Render the delete confirmation template
