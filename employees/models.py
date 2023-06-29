from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    identification_document = models.FileField(upload_to='employee_documents/', null=True, blank=True)
    # Add other fields as per requirements

    def __str__(self):
        return self.name