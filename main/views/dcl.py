from django.shortcuts import render
from django.views import View
from ..forms import TaskForm
from ..models.task import Task

class Dcl(View):
    def get(self, request):
        task = TaskForm()
        context = {'task': task}
        return render(request, 'dcl.html', context)

    def post(self, request, *args, **kargs):
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            # print(task)
        #tasks_list = Task.objects.all()
        #context = {'task_list': tasks_list}
        #return render(request, 'tasks.html', context)
