from django.contrib import admin
from .models import Application, Cycle, Stage, Cycle_Stage_Link, CycleStageRoute, PostponeCourseDocument
# Register your models here.
admin.site.register(Application)
admin.site.register(Cycle)
admin.site.register(Stage)
admin.site.register(Cycle_Stage_Link)
admin.site.register(CycleStageRoute)
admin.site.register(PostponeCourseDocument)
