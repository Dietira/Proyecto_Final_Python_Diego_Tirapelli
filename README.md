# Proyecto Final  -- DiegoTirapelli

## App para adopción de mascotas

## Descripción
Este proyecto es una aplicación web de adopción de mascotas creada con Django y Python. Los usuarios pueden ver mascotas disponibles para adopción, marcar mascotas como favoritas y enviar solicitudes de adopción.

## Características
## Modelos Principales

El proyecto consta de varios modelos principales:

- `Avatar`: Cada usuario tiene un avatar asociado.
- `Raza`: Define las diferentes razas de mascotas disponibles.
- `Mascota`: Representa a las mascotas disponibles para adopción.
- `Mascotas_Favoritas`: Permite a los usuarios marcar mascotas como favoritas.
- `Solicitud_Adopcion`: Los usuarios pueden enviar solicitudes de adopción para mascotas.


## Tecnologías Utilizadas
- **Python**: 3.10.7
- **Django**: 5.0.2
- **Pillow**: 10.2.0

## Configuración del Proyecto
Para configurar y ejecutar el proyecto en tu entorno local, sigue estos pasos:

1. Realiza las migraciones para configurar la base de datos:

   `python manage.py makemigrations`

   `python manage.py migrate`

2. Si lo deseas puedes crear un superusuario para acceder al panel de administración de Django:

    `python manage.py createsuperuser`
El usuario administrador que se creo fue
user: super_user
pass: python123

3. Inicia el servidor de desarrollo:

   `python manage.py runserver`

4. Ahora deberías poder acceder a la aplicación en `localhost:8000`.

## URLs de la Aplicación

- **Inicio**: `http://127.0.0.1:8000/` - Página principal de la aplicación.
- **Registro**: `registro/` - Para registrarse en la aplicacion.
- **Loguin**: `loguin/` - Para acceder a las funcionalidades de la aplicacion.
- **Logout**: `logout/` - Para cerrar la aplicacion.
- **About**: `about/` - Muestra el acerca de mi.
- **Editar perfil**: `editar_perfil/` - Permite cambiar la foto y los datos relacionados al registro del usuario.
- **Contraseña**: `contra/` - Para cambiaar la contraseña del usuario.
- **Crear raza**: `rear_raza/` - Define las razas de los diferentes animales en adopcion.
- **Listar raza**: `listar_raza/` - Lista todas las razas disponibles para clasificar a los animales.
- **Editar una raza**: `editar_raza/` - Edita una raza seleccionada para cambiarle propiedades.
- **Eliminar_Raza**: `elimiar_raza/` - Permite eliminar una raza seleccionada.
- **Crear_Mascota**: `crear_mascota/` - Da de alta en el sistema una nueva mascota para adoptar.
- **Listar Mascota**: `listar_mascota/` - Lista todas las mascotas cargadas en el sistema.
- **Editar Mascota**: `Editar_Mascota/` - Edita una mascota seleccionada para cambiarle propiedades.
- **Eliminar Mascota**: `Eliminar_Mascota/` - Permite eliminar una mascota seleccionada.
- **En_Adopcion**: `en_adopcion/` - Muestra todas las mascotas disponibles para adoptar.
- **Eliminar Mascota**: `Eliminar_Mascota/` - Permite eliminar una mascota seleccionada.
- **Detalle_Mascota**: `detalle_mascota/` - Permite ver los detalles de la mascota seleccionada.
- **Agregar a favoritos**: `agregar_favorito/` - Agrega una mascota a una lista de mascotas favoritas.
- **Listar Favoritos**: `listar_favorito/` - Muestra todas las mascotas clasificadas como favoritos del usuario.
- **Eliminar Favorito**: `elimiar_favorito/` - Quita de favoritos una mascota.
- **Crear Solicitud**: `crear_solicitud/` - Crea una solicitud de adopcion la cual quedara pendiente de aprobacion.
- **Editar Solicitud**: `editar_solicitud/` - Permite cambiar el estado de la solicitud a aprobada, rechazada, y dar una respuesta al usuario.
- **Listar Solicitud**: `listar_solicitud/` - Muestra las solicitudes cargadas en el sistema.
- **Eliminar Solicitud**: `elimiar_solicitud/` - Elimina una solicitud creada.

## Uso de la Aplicación
De acuerdo con el tipo de usuario logueado, algunas opciones no estarán disponibles. 
Navega por las URLs indicadas para acceder a las diferentes funcionalidades de la aplicación. Sigue las instrucciones en pantalla para realizar las acciones deseadas, como ver las mascotas disponibles para adoptar, marcar algunas como favoritas y solicitar la adopcion de alguna de ellas.

