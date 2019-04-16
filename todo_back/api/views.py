from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer


# Create your views here.

def index(request):
    return HttpResponse('<h1>Index page</h1>')


def about(request):
    return HttpResponse('<h1>About page</h1>')


def get_task_list(request, list_id):
    try:
        task_list = TaskList.objects.get(id=list_id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json())


def get_tasks_in_list(request, list_id):
    tasks = Task.objects.all()
    response = []
    for task in tasks:
        if task.task_list.id == list_id:
            response.append(task.to_part_json())

    return JsonResponse(response, safe=False)


def get_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task.to_json())


def list_task_list(request):
    tasklists = TaskList.objects.all()

    json_tasklists = [t.to_json() for t in tasklists]
    return JsonResponse(json_tasklists, safe=False)
