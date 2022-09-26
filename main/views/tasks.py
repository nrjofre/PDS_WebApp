from django.shortcuts import render
from django.views import View
from ..models.tarea import Tarea
from main.models import tarea

class Tasks(View):
    def get(self, request):
        #tasks_list = Tarea.objects.all()
        context = {'task_list': tasks_list}
        return render(request, 'tasks.html', context)
