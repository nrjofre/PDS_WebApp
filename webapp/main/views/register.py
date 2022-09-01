from django.shortcuts import render, redirect
from main.forms import RegisterForm
from django.views import View


# Create your views here.
class Register(View):
    def post(self, request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/")
        else:
            form = RegisterForm()

        return render(request, "register/register.html", {"form": form})

    def get(self, request):
        form = RegisterForm()
        return render(request, "register/register.html", {"form": form})
