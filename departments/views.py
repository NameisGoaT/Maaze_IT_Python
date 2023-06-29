from django.shortcuts import render

# Create your views here.
from django.db import connection
from rest_framework import generics
from .models import Department
from .serializers import DepartmentSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM departments_department")
        return cursor.fetchall()

    def perform_create(self, serializer):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO departments_department (name) VALUES (%s)", [serializer.validated_data['name']])

