from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=14)
    national_id = models.CharField(max_length=14)