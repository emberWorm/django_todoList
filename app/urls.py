from django.urls import path
from .views import *

urlpatterns = [
    # path('route/', function)
    path('hello_world/', hello_world),
    path('todos/', todos),
    path('add_todo/', add_todo),
    path('delete_todo/<int:todo_id>', delete_todo),
    path('check_todo/<int:todo_id>', check_todo),
    path('edit_todo/<int:todo_id>', edit_todo),
]

