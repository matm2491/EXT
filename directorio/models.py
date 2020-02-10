from django.db import models

# importo los modelos de la base de datos de postgres ya creados buscandolos con el comando (manage.py inspectdb)

class TinDependencias(models.Model):
    dependencia_id = models.IntegerField(unique=True, blank=True, null=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    localidad = models.CharField(max_length=1, blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    estatus = models.IntegerField(blank=True, null=True)
    organigrama = models.BooleanField(blank=True, null=True)
    codigo_domesa = models.CharField(max_length=1, blank=True, null=True)
    direccion = models.CharField(max_length=80, blank=True, null=True)
    telefonos = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    cubierto_domesa = models.BooleanField()
    vigente = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tin_dependencias'



class TinUsuarios(models.Model):
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    trabajador_id = models.IntegerField()
    cargo_id = models.IntegerField(blank=True, null=True)
    dependencia_id = models.IntegerField(blank=True, null=True)
    manual_cargo_id = models.IntegerField(blank=True, null=True)
    descripcion_cargo = models.CharField(max_length=120, blank=True, null=True)
    grado = models.IntegerField(blank=True, null=True)
    cedula = models.IntegerField(blank=True, null=True)
    primer_nombre = models.CharField(max_length=30, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    primer_apellido = models.CharField(max_length=30, blank=True, null=True)
    segundo_apellido = models.CharField(max_length=30, blank=True, null=True)
    correo_inst = models.CharField(max_length=60, blank=True, null=True)
    correo_personal = models.CharField(max_length=60, blank=True, null=True)
    estatus = models.CharField(max_length=1, blank=True, null=True)
    tipo_personal_id = models.IntegerField(blank=True, null=True)
    des_tipo_personal = models.CharField(max_length=120, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True)
    clave = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    fecha_clave = models.DateTimeField()
    tin_parroquia_id = models.IntegerField(blank=True, null=True)
    zona_postal = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    tlf_extension = models.CharField(max_length=20, blank=True, null=True)
    tlf_personal = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    fecha_egreso = models.DateField(blank=True, null=True)
    salt = models.CharField(max_length=1, blank=True, null=True)
    tlf_local = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return "%s %s" % (self.primer_nombre, self.primer_apellido)


    class Meta:
        managed = False
        db_table = 'tin_usuarios'

