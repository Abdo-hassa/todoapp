from django.shortcuts import render,redirect
from .models import Todolist
from .forms import TodoListForm
from django.urls import reverse
from django.views.decorators.http import require_POST
def home(request):
    todo_items=Todolist.objects.order_by('id')
    form=TodoListForm()
    context = {"todo_items":todo_items,'form':form}
    return render(request,'todolist/bbbootstrap-snippet.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo=Todolist(text=request.POST['text'])
        new_todo.save()

    return redirect('home')


def completedTodo(request,todo_id):
    todo=Todolist.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()
    return redirect('home')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()

    return redirect('home')
def deleteAll(request):
    Todolist.objects.all().delete()

    return redirect('home')
