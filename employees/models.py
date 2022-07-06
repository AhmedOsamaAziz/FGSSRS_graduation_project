from operator import truediv
from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    mobile = models.CharField(max_length=14, null=True, blank=True)
    national_id = models.CharField(max_length=14, null=True, blank=True)
    
    def __str__(self):
        return self.emp_name
