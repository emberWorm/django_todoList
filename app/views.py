from django.shortcuts import render, redirect
from .models import Todo


def hello_world(request):
    return render(request, "index.html")


def todos(request):
    todos_list = Todo.objects.all().order_by("-id")
    return render(request, "todos.html", {"todos": todos_list})


def add_todo(request):
    new_todo = request.POST["todo-title"]

    Todo.objects.create(title=new_todo, completed=False)

    return redirect("/app/todos/")


def check_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    todo.completed = not todo.completed
    todo.save()

    return redirect("/app/todos/")

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todos_list = Todo.objects.all().order_by("-id")

    if request.GET.get("confirm") == "true":
        todo.delete()
        return redirect("/app/todos/")

    return render(
        request,
        "todos.html",
        {"todos": todos_list, "action": "delete", "todo_id": todo_id}
    )

def edit_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todos_list = Todo.objects.all().order_by("-id")

    if request.method == "POST":
        todo.title = request.POST["todo-title"]
        todo.save()
        return redirect("/app/todos/")

    return render(
        request, "todos.html", {"todo_object": todo, "action": "edit", "todos": todos_list}
    )
