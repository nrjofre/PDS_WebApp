from django.shortcuts import render
from django.views import View
from ..models.task import Task
from main.models import task 

class Tasks(View):
    def get(self, request):
        tasks_list = Task.objects.all()
        context = {'task_list': tasks_list}
        return render(request, 'tasks.html', context)
