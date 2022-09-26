from atexit import register
from django.contrib import admin
from django.urls import path, include
from . import views
from .views.student import drawDcl, selectDcl, ddcl, equations

urlpatterns = [
    path('register/', views.Register.as_view(), name="register"),
    path('', views.Index.as_view(), name="index"),
    path('dcl/', views.Dcl.as_view(), name="dcl"),
    path('tasks/', views.Tasks.as_view(), name="tasks"),
    path('draw/', drawDcl.DrawDcl.as_view(), name="draw"),
    path('divide/', selectDcl.SelectDcl.as_view(), name="divide"),
    path('ddcl/', ddcl.DDcl.as_view(), name="ddcl"),
    path('eq/', equations.Equations.as_view(), name="eq"),
    path('ctask/', views.CTask.as_view(), name="ctask"),
    path('users/', views.Users.as_view(), name="users"),
    path('ctask/<task_id>', views.CTask.edit, name="edit_task"),
    path('delete_task/<task_id>', views.CTask.delete_task, name="delete_task"),
]
