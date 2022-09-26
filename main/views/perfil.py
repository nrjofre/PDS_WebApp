from main.views.users import Users
from django.shortcuts import render
from django.views import View
from ..models.profile import Profile


class Perfil(View):
    def get(self, request, user_id):
        profile = Profile.objects.get(user=user_id)
        context = {'profile': profile}
        return render(request, 'profile.html', context)

