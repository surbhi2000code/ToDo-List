from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import drone
from .forms import *


# Create your views here.

def index(request):
    tasks = drone.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task': tasks, 'form': form}
    return render(request, "list.html", context)


def updateTask(request, pk):
    task = drone.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = drone.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'delete.html', context)