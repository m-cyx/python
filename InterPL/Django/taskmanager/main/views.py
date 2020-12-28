from django import forms
from django.shortcuts import render
from .models import Task
#from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-id') # это будет список
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
#    form = TaskForm()
#    context = {
#        'form': form
#    }
    #return render(request, 'main/create.html', context)
    return render(request, 'main/create.html')