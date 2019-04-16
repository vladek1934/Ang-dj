from rest_framework import serializers
from .models import TaskList, Task


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    status = serializers.CharField(required=True)
    task_list = TaskListSerializer(required=True)

    class Meta:
        model = Task
        fields = '__all__'
