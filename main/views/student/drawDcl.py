from django.shortcuts import render
from django.views import View

class DrawDcl(View):
    def get(self, request):
        context = {}

        return render(request, 'student/drawDcl.html', context)
