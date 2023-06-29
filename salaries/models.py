
from django.db import models
from employees.models import Employee

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other fields as per requirements

    def __str__(self):
        return f"{self.employee.name}'s Salary"