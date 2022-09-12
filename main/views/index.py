from django.shortcuts import render
from django.views import View


class Index(View):
    def get(self, request):

        context = {}
        return render(request, 'index.html', context)
