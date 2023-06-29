from django.shortcuts import render
from django.db import connection
from rest_framework import generics
from .models import Salary
from .serializers import SalarySerializer

class SalaryListCreateView(generics.ListCreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM salaries_salary")
        return cursor.fetchall()

    def perform_create(self, serializer):
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO salaries_salary (employee_id, amount) VALUES (%s, %s)",
            [serializer.validated_data['employee'], serializer.validated_data['amount']]
        )

