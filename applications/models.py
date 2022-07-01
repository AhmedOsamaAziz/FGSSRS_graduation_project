from django.db import models


from generic.models import Person
# Create your models here.

class Cycle(models.Model):
    cycle_name = models.CharField(max_length=50)

class Stage(models.Model):
    stage_name = models.CharField(max_length=50)

class Cycle_Stage_Link(models.Model):
    cycle_id = models.ForeignKey(Cycle,on_delete=models.PROTECT,related_name='application')
    stage_id = models.ForeignKey(Stage,on_delete=models.PROTECT,related_name='application')


class Application(models.Model):
    person_id = models.ForeignKey(Person,on_delete=models.PROTECT,related_name='application')
    current_statge_link_id = models.ForeignKey(Cycle_Stage_Link,on_delete=models.PROTECT,related_name='application')

