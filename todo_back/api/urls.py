from django.urls import path, re_path
from api import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('api/task_lists/', views.list_task_list),
    path('api/task_lists/<int:list_id>/', views.get_task_list),
    path('api/task_lists/<int:list_id>/tasks', views.get_tasks_in_list),
    path('api/tasks/<int:task_id>', views.get_task)

]
