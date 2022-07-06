from django.db import models
from students.models import Student
from employees.models import Employee

from generic.models import Person
# Create your models here.

class Cycle(models.Model):
    cycle_name = models.CharField(max_length=50)
    document = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.cycle_name

class Stage(models.Model):
    stage_name = models.CharField(max_length=50)

    def __str__(self):
        return self.stage_name

class Cycle_Stage_Link(models.Model):
    cycle_id = models.ForeignKey(Cycle,on_delete=models.PROTECT,related_name='stages')
    stage_id = models.ForeignKey(Stage,on_delete=models.PROTECT,related_name='cyclelinked')
    is_init = models.BooleanField(default=False)
    
    def __str__(self):
        return self.cycle_id.cycle_name + ' -> ' + self.stage_id.stage_name  


class Application(models.Model):
    application_number = models.CharField(max_length=6, null=True, blank=True)
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='applications')
    current_employee_id = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='applications', null=True,
                                            blank=True)
    current_cycle_stage_link_id = models.ForeignKey(Cycle_Stage_Link, on_delete=models.PROTECT,
                                                    related_name="applications", null=True, blank=True)

    def __str__(self):
        return self.application_number


class CycleStageRoute(models.Model):
    cycle_stage_link_id = models.ForeignKey(Cycle_Stage_Link, on_delete=models.PROTECT, related_name='routes')
    next_Cycle_stage_link_id = models.ForeignKey(Cycle_Stage_Link, on_delete=models.PROTECT, related_name='nextroutes')

    def __str__(self):
        return f'{self.cycle_stage_link_id} -> {self.next_Cycle_stage_link_id.stage_id.stage_name}'


class PostponeCourseDocument(models.Model):
    subject_name = models.CharField(max_length=150)
    postpone_reason = models.TextField(max_length=255)
    application_id = models.ForeignKey(Application, on_delete=models.PROTECT, related_name='postponed_documents')

