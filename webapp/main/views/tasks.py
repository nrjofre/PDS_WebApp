from django.shortcuts import render
from django.views import View

class Tasks(View):
    def get(self, request):
        context = {}
        return render(request, 'tasks.html', context)
