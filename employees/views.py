# from django.shortcuts import render
# from django.db import connection
# from rest_framework import generics
# from .models import Employee
# from .serializers import EmployeeSerializer

# class EmployeeListCreateView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get_queryset(self):
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM employees_employee")
#         return cursor.fetchall()

#     def perform_create(self, serializer):
#         cursor = connection.cursor()
#         cursor.execute(
#             "INSERT INTO employees_employee (name, department_id) VALUES (%s, %s)",
#             [serializer.validated_data['name'], serializer.validated_data['department']]
#         )



# employees/views.py

from django.db import connection
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees_employee")
        rows = cursor.fetchall()
        employees = [Employee(id=row[0], name=row[1]) for row in rows]
        return employees

    def perform_create(self, serializer):
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO employees_employee (name, department_id) VALUES (%s, %s)",
            [serializer.validated_data['name'], serializer.validated_data['department']]
        )
