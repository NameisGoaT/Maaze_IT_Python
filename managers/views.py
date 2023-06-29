from django.shortcuts import render

# Create your views here.
from django.db import connection
from rest_framework import generics
from .models import Manager
from .serializers import ManagerSerializer

class ManagerListCreateView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM managers_manager")
        return cursor.fetchall()

    def perform_create(self, serializer):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO managers_manager (name) VALUES (%s)", [serializer.validated_data['name']])
