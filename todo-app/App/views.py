from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='/accounts/login')
def index(request):
    todos = Todo.objects.filter(creater=request.user)
    # todos = Todo.objects
    return render(request, 'App/index.html', {'todos': todos})

@login_required(login_url='/accounts/login')
def create(request):
    if request.method == "POST":
        if request.POST['name']:
            todo = Todo()

            todo.name = request.POST['name']
            todo.date = timezone.now()
            todo.creater = request.user

            todo.save()
            return redirect('home')
        else:
            return render(request, 'App/create.html', {'err': 'Todo name must be specified.'})
    else:
        return render(request, 'App/create.html')

@login_required(login_url="/accounts/login")
def edit(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'App/edit.html', {'todo': todo})

@login_required(login_url="/accounts/login")
def delete_task(request, todo_id):
    if request.method == "POST":
        # todo = Todo.objects.get(pk=todo_id)
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()
        return redirect('home')

@login_required(login_url="/accounts/login")
def update(request, todo_id):
    if request.method == "POST":
        # todo = Todo.objects.get(pk=todo_id)
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.name = request.POST["name"]
        todo.save()
        return redirect('home')
