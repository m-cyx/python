from django import forms
from django.shortcuts import render, redirect
from django.forms import ModelForm
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-id') # это будет список
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Неверная форма'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def delete(request):
    return render(request, 'main/delete.html')
    #return render(request, 'main/create.html')