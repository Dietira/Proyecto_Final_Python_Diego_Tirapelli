from django.urls import path
from app_proyecto.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio, name= "Home"),
    path("registro/",registro, name= "Registrar"),
    path("loguin/",iniciar_sesion, name= "Loguin"),
    path("logout/", salir, name="Salir"),
    path("about/", about, name="About"),
    path('editar_perfil/', editarPerfil, name="Editar_Perfil"), 
    path("contra/", cambiar_contra.as_view(), name="Cambiar_Contra"),

    # CRUD RAZA
    path("crear_raza/", crear_raza, name="Crear_Raza"),
    path("listar_raza/", listar_razas, name="Listar_Raza"),
    path("editar_raza/<id_raza>/", editar_raza, name="Editar_Raza"),
    path("elimiar_raza/<id_raza>/", eliminar_raza, name="Eliminar_Raza"),

    # CRUD MASCOTA
    path("crear_mascota/", crear_mascota, name="Crear_Mascota"),
    path("listar_mascota/", listar_mascotas, name="Listar_Mascota"),
    path("editar_mascota/<id_mascota>/", editar_mascota, name="Editar_Mascota"),
    path("elimiar_mascota/<id_mascota>/", eliminar_mascota, name="Eliminar_Mascota"),
    path("en_adopcion/", mascotas_disponibles, name="En_Adopcion"),
    path("detalle_mascota/<id_mascota>/", detalle_mascota, name="Detalle_Mascota"),

     # CRUD FAVORITO
     path("agregar_favorito/<id_mascota>/", agregar_favorito, name="agregar_favorito"),
     path("listar_favorito/", listar_favoritos, name="Listar_Favorito"),     
     path("elimiar_favorito/<id_favorito>/", eliminar_favorito, name="Eliminar_Favorito"),


     # CRUD SOLICITUDES DE ADOPCION
     path("crear_solicitud/<id_mascota>/", crear_solicitud, name="Crear_Solicitud"),
     path("editar_solicitud/<id_solicitud>/", editar_solicitud, name="Editar_Solicitud"),
     path("listar_solicitud/", listar_solicitudes, name="Listar_Solicitud"),     
     path("elimiar_solicitud/<id_solicitud>/", eliminar_solicitud, name="Eliminar_Solicitud"),
]
