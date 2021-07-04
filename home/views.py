from django.http import request
from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.edit import CreateView
from .forms import SignUpForm, TodoForm
from django.urls import reverse_lazy
from .models import Todo

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Index(request):
    
    if request.method == 'POST':
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit = False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {'form': form})

    else:

        if request.user.is_authenticated:
            user = request.user
        
            form = TodoForm()
            todos = Todo.objects.filter(user = user)

            context = {
                'form': form,
                'todos': todos
            }

            return render(request, 'index.html', context)
        
        else:
            form = TodoForm()
            todos = Todo.objects.all()

            context = {
                'form': form,
                'todos': todos
            }

            return render(request, 'index.html', context)

def delete_task(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('home')

def change_status(request, id, status):
    todo = Todo.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

def Upcoming(request):

    if request.user.is_authenticated:
            user = request.user
            todos = Todo.objects.filter(user = user)
            
            data = {
                'todos': todos
            }

            return render(request, "upcoming.html", data)
