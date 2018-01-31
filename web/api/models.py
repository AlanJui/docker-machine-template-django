from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    employee_id = models.IntegerField()

    def __str__(self):
        return self.first_name
