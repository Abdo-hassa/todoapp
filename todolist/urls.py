
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add',views.addTodoItem,name='add'),
    path('completed\<todo_id>',views.completedTodo,name='completedd'),
    path('deletecompleted',views.deleteCompleted,name='deletecompleted'),
    path('deleteall',views.deleteAll,name='deleteall'),



]
