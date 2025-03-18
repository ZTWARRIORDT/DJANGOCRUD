from django.contrib import admin
from .models import Tasks
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    ## Cuales campos son de lectura o cuales quiero ver al momento de crear la tarea en el modo admin. Se coloca la coma porque es una tupla
    readonly_fields = ("created", )

admin.site.register(Tasks, TaskAdmin)