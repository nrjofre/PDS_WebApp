from django.shortcuts import render, redirect
from django.views import View
from ..forms import TaskForm
from ..models.task import Task
from ..models.tarea import Tarea

class Dcl(View):
    def get(self, request, task_id):
        task = TaskForm()
        context = {'task': task, 'task_id': task_id}
        return render(request, 'dcl.html', context)

    def post(self, request, *args, **kargs):
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return redirect('../tasks')
