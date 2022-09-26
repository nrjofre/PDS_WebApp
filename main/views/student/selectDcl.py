from django.shortcuts import render
from django.views import View

from main.models.tarea import Tarea

class SelectDcl(View):
    def get(self, request, task_id):
        task = Tarea.objects.get(id=task_id)
        context = {'task': task}

        return render(request, 'student/selectDcl.html', context)
