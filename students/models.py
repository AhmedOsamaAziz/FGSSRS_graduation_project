from django.db import models

from generic.models import Person
# Create your models here.

class Study_Type(models.Model):
    study_type = models.CharField(max_length=100)

    def __str__(self):
        return self.study_type


class Study_Specialize(models.Model):
    study_specialize = models.CharField(max_length=50)

    def __str__(self):
        return self.study_specialize


class Student(models.Model):

    name = models.CharField(max_length=100)
    term_no = models.IntegerField()
    student_code = models.IntegerField()
    overall_rating = models.CharField(max_length=20)
    # One To Many Relashionship --> ForeignKey
    study_type_id = models.ForeignKey(Study_Type, on_delete=models.PROTECT, related_name='students')
    study_specialize_id = models.ForeignKey(Study_Specialize, on_delete=models.PROTECT,related_name='students')
    person_id = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='students')

    def __str__(self):
            return self.name
