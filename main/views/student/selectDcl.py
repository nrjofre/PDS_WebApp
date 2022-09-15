from django.shortcuts import render
from django.views import View

class SelectDcl(View):
    def get(self, request):
        context = {}

        return render(request, 'student/selectDcl.html', context)
