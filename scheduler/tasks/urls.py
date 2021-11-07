from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('view_all_tasks', views.view_all_tasks, name='view_all_tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('view_all_notes', views.view_all_notes, name='view_all_notes'),
    path('new_one', views.new_one, name='new_one')
]
