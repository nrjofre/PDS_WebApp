from django.shortcuts import render
from django.views import View

class Dcl(View):
    def get(self, request):
        context = {}
        return render(request, 'dcl.html', context)

    def post(self, request, *args, **kargs):
        print(request.POST)
        return render(request, 'tasks.html')
