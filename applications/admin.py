from django.contrib import admin
from .models import Cycle,Stage,Cycle_Stage_Link,Documents,Application

# Register your models here.
admin.site.register(Cycle)
admin.site.register(Stage)
admin.site.register(Cycle_Stage_Link)
admin.site.register(Documents)
admin.site.register(Application)
