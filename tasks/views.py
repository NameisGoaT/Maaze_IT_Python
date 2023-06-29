from django.shortcuts import render
from django.db import connection
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks_task")
        return cursor.fetchall()

    def perform_create(self, serializer):
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO tasks_task (name, employee_id) VALUES (%s, %s)",
            [serializer.validated_data['name'], serializer.validated_data['employee']]
        )

