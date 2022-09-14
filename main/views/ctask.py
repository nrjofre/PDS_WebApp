from django.shortcuts import render, redirect
from django.views import View

from main.forms import CreateTaskForm

class CTask(View):
    def get(self, request):
        form = CreateTaskForm()
        return render(request, "ctask.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = CreateTaskForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = CreateTaskForm()

        return render(request, "ctask.html", {"form": form})

