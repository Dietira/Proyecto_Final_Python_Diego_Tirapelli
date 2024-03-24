from django.contrib import admin
from app_proyecto.models import *
# Register your models here.
admin.site.register(Avatar)
admin.site.register(Raza)
admin.site.register(Mascota)
admin.site.register(Mascotas_Favoritas)
admin.site.register(Solicitud_Adopcion)

