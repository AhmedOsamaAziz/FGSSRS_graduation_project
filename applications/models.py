from django.db import models


from generic.models import Person
# Create your models here.

class Cycle(models.Model):
    cycle_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cycle_name

class Stage(models.Model):
    stage_name = models.CharField(max_length=50)

    def __str__(self):
        return self.stage_name


class Cycle_Stage_Link(models.Model):
    cycle_id = models.ForeignKey(Cycle,on_delete=models.PROTECT,related_name='application')
    stage_id = models.ForeignKey(Stage,on_delete=models.PROTECT,related_name='application')

class Documents(models.Model):
    name = models.CharField(max_length=100)
    tabel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Application(models.Model):
    
    current_statge_link_id = models.ForeignKey(Cycle_Stage_Link,on_delete=models.PROTECT,related_name='application')
    current_employee_id = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='application')
    #student_id = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='application')
    document_id = models.ForeignKey(Documents,on_delete=models.PROTECT,related_name='application')


