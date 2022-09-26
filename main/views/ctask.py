from django.shortcuts import render, redirect
from django.views import View

from main.forms import CreateTaskForm
from ..models.tarea import Tarea

class CTask(View):
    def get(self, request):
        form = CreateTaskForm()
        return render(request, "ctask.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = CreateTaskForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                tasks_list = Tarea.objects.all()
                context = {'task_list': tasks_list}
                return redirect('/tasks')
        else:
            form = CreateTaskForm()

        return render(request, "ctask.html", {"form": form})

    def edit(request, task_id):
        task = Tarea.objects.get(id=task_id)
        form = CreateTaskForm(instance=task)
        if request.method == "POST":
            form = CreateTaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                tasks_list = Tarea.objects.all()
                context = {'task_list': tasks_list}
                return redirect('/tasks')
        else:
            form = CreateTaskForm(instance=task)

        return render(request, "ctask.html", {"form": form})

    def delete_task(request, task_id):
        task = Tarea.objects.get(id=task_id)
        if request.method == "POST":
            task.delete()
            return redirect('/tasks')
        return render(request, "delete_task.html", {"task": task})

