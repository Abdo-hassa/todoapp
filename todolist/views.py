from django.shortcuts import render

def home(request):
	return render(request,'todolist/bbbootstrap-snippet.html')
