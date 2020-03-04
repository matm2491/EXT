from django.db import models

# Create your models here.

class TinDependencias(models.Model):
    descripcion = models.CharField(max_length=150, blank=True, null=True)
   


    def __str__(self):
        return "%s" % (self.descripcion)

    

    class Meta:
        managed = False
        db_table = 'tin_dependencias'

