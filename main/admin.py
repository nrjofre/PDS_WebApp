from django.contrib import admin
from .models import Task, Tarea, Profile

# Register your models here.
admin.site.register(Task)
admin.site.register(Tarea)
admin.site.register(Profile)