from django.shortcuts import render
from django.views import View

class Equations(View):
    def get(self, request):
        context = {}

        return render(request, 'student/equations.html', context)
