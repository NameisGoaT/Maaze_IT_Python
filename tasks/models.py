from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE)
    # Add other fields as per requirements

    def __str__(self):
        return self.name