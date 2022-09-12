from django.shortcuts import render
from django.views import View
from ..forms import TaskForm

class Dcl(View):
    def get(self, request):
        task = TaskForm()
        context = {'task': task}
        return render(request, 'dcl.html', context)

    def post(self, request, *args, **kargs):
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            print("Saved correctly.")
        context = {}
        return render(request, 'tasks.html', context)
