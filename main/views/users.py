from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required


class Users(View):
    def get(self, request):
        users_list = User.objects.all()
        context = {'users_list': users_list}
        return render(request, 'users.html', context)