from django.shortcuts import render
from .models import Todolist

def home(request):
    todo_items=Todolist.objects.order_by('id')
    context = {"todo_items":todo_items}
    return render(request,'todolist/bbbootstrap-snippet.html',context)
