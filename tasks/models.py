from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    ### Añade la fecha y la hora por defecto
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    """
    EL models.CASCADE es para eliminar en casacada los datos, es decir, 
    si borro el ususario, todas las tareas relacionadas
    con ese usuario tambien se borran.
    """
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.title + ' - ' + self.user.username)