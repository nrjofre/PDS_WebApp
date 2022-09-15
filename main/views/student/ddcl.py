from django.shortcuts import render
from django.views import View

class DDcl(View):
    def get(self, request):
        context = {}

        return render(request, 'student/ddcl.html', context)
