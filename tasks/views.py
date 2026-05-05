from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

# def index(request):
    
#     form = TaskForm()
    
#     tasks = task.objects.all()
    
#     if request.method == "POST":
#         form = TaskForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             form = TaskForm()
#         return redirect('/')
    
#     context = {
#         'tasks': tasks,
#         'TaskForm': form
#         }
    
#     return render(request, 'tasks.html', context)

class index(LoginRequiredMixin, View):
    def get(self, request):
        form = TaskForm()
    
        tasks = task.objects.filter(user=request.user)
    
        context = {
            'tasks': tasks,
            'TaskForm': form
        }
    
        return render(request, 'tasks.html', context)

    def post(self, request):
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task_instance = form.save(commit=False)
            task_instance.user = request.user
            task_instance.save()
            form = TaskForm()
        return redirect('/')


# def updateTask(request, pk):
#     task_obj = task.objects.get(id=pk)
#     form = TaskForm(instance=task_obj)

#     if request.method == "POST":
#         form = TaskForm(request.POST, instance=task_obj)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {
#         'TaskForm': form
#     }

#     return render(request, 'update-task.html', context)

class updateTask(LoginRequiredMixin, View):
    def get(self, request, pk):
        task_obj = task.objects.get(id=pk)
        form = TaskForm(instance=task_obj)

        context = {
            'TaskForm': form
        }

        return render(request, 'update-task.html', context)

    def post(self, request, pk):
        task_obj = task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            form.save()
            return redirect('/')



# def deleteTask(request, pk):
#     task_obj = task.objects.get(id=pk)
#     if request.method == "POST":
#         task_obj.delete()
#         return redirect('/') 
    
#     context = {
#         'task': task_obj
#     }
    
#     return render(request, 'delete-task.html', context)

class deleteTask(LoginRequiredMixin, View):    
    def get(self, request, pk):
        task_obj = task.objects.get(id=pk)
    
        context = {
            'task': task_obj
        }
    
        return render(request, 'delete-task.html', context)

    def post(self, request, pk):
        task_obj = task.objects.get(id=pk)
        task_obj.delete()
        return redirect('/')
    
class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')    