from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as per requirements

    def __str__(self):
        return self.name
