from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_proyecto.models import *
from app_proyecto.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST


# Create your views here.
def inicio(request):
    return render(request,"app_proyecto/inicio.html", {"mensaje": ""})

def about(request):
    return render(request,"app_proyecto/about.html")

# VISTAS PARA INICIO, REGISTRO, LOGUOT DE SESION Y EDICION PERFIL
def iniciar_sesion(request):
    if request.method == "POST":

        formulario = AuthenticationForm(request, data = request.POST) #almacena la informacion que se ha puesto en el form

        if formulario.is_valid():

            info_dic = formulario.cleaned_data #convierte la info del form a un diccionario de python

            usuario = authenticate(username=info_dic["username"], password=info_dic["password"])

            if usuario is not None: #que el usuario existe!!!

                login(request, usuario)

                return render(request, 'app_proyecto/inicio.html', {"mensaje":f"Bienvenido {usuario}"})
        else:
            return render(request, 'app_proyecto/inicio.html', {"mensaje":"Credenciales Incorrectas"})
    else:
        formulario = AuthenticationForm()
    return render(request, 'registro/loguin.html', {"formulario":formulario})


def registro(request):
    if request.method == "POST":
        form = Usuario_Registro(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user =form.save()
            Avatar.objects.create(usuario=user, imagen='default.png')
            return render(request,'app_proyecto/inicio.html',{"mensaje":"Registro exitoso !!!"})
    else:
        form = Usuario_Registro()
    return render(request, 'registro/registro.html', {'formulario': form})

@login_required        
def salir(request):
    logout(request)
    return redirect('Home')


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = Usuario_Editar_Perfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():

            informacion = formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
           
            if 'imagen' in request.FILES:
                avatar = Avatar.objects.get(usuario=usuario)
                avatar.imagen = request.FILES['imagen']
                avatar.save()
    
            return render(request, "app_proyecto/inicio.html")
    else:
        if hasattr(usuario, 'avatar'):  # Comprueba si el usuario tiene un avatar
            imagen = usuario.avatar.imagen
        else:
            # Crea y asigna un nuevo avatar al usuario
            avatar = Avatar(imagen='default.png', usuario=usuario)
            avatar.save()
            imagen = avatar.imagen
        formulario = Usuario_Editar_Perfil(initial={
                    'email': usuario.email,
                    'last_name': usuario.last_name,
                    'first_name': usuario.first_name,
                    'imagen': imagen}, instance=request.user)
    return render(request, "registro/editar_Perfil.html", {"formulario": formulario, "usuario": usuario})

class cambiar_contra(LoginRequiredMixin, PasswordChangeView):
    template_name = "registro/cambiar_contra.html"
    success_url = "/"

# CRUD DEl MODELO RAZA BASADO EN DEFINICIONES

@login_required
def crear_raza(request):
    if request.method == "POST":
        formulario = Raza_Form(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nueva_raza = Raza( nombre = info['nombre'],
                            origen = info['origen'],
                            tamanio_promedio = info['tamanio_promedio'],
                            esperanza_de_vida = info['esperanza_de_vida'],
                            descripcion = info['descripcion'])
            nueva_raza.save()
            return render(request, 'app_proyecto/inicio.html')        
    else:
        formulario = Raza_Form()
    return render(request, "raza/crear_raza.html", {"formulario":formulario})

@login_required
def listar_razas(request):
    razas = Raza.objects.all()
    return render(request, "raza/listar_raza.html", {"razas":razas})

@login_required
def editar_raza(request, id_raza):
    raza = Raza.objects.get(id=id_raza)
    if request.method == "POST":
        formulario = Raza_Form(request.POST) 
        if formulario.is_valid():
            info = formulario.cleaned_data
            raza.nombre= info['nombre']
            raza.origen = info['origen']
            raza.tamanio_promedio = info['tamanio_promedio']
            raza.esperanza_de_vida = info['esperanza_de_vida']
            raza.descripcion = info['descripcion']
            raza.save()
            return render(request, 'app_proyecto/inicio.html')        
    else:
        formulario = Raza_Form(initial={
                    'nombre':raza.nombre, 
                    'origen':raza.origen,
                    'tamanio_promedio':raza.tamanio_promedio,
                    'esperanza_de_vida':raza.esperanza_de_vida, 
                    'descripcion':raza.descripcion})
    return render(request, "raza/editar_raza.html", {"formulario":formulario , "raza": raza})

@login_required
def eliminar_raza(request, id_raza):
    raza = Raza.objects.get(id=id_raza)
    raza.delete()
    return render(request, "app_proyecto/inicio.html")


# CRUD DEl MODELO MASCOTA BASADO EN DEFINICIONES

@login_required
def crear_mascota(request):
    if request.method == "POST":
        formulario = Mascota_Form(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nueva_mascota = Mascota( 
                            nombre = info['nombre'],
                            raza = info['raza'],
                            descripcion = info['descripcion'],
                            foto = info['foto']
                          )
            nueva_mascota.save()            
            return render(request, 'app_proyecto/inicio.html')        
    else:
        formulario = Mascota_Form()
    razas = Raza.objects.all()
    return render(request, "mascota/crear_mascota.html", {"formulario":formulario , 'razas': razas})

@login_required
def listar_mascotas(request):
    filtro = request.GET.get('search', '')
    if filtro:
        mascotas = Mascota.objects.filter(raza__nombre__icontains=filtro)
    else:
        mascotas = Mascota.objects.all()
    return render(request, "mascota/listar_mascota.html", {"mascotas": mascotas})

@login_required
def mascotas_disponibles(request):
    mascotas = Mascota.objects.filter(disponible=True)
    return render(request, "mascota/mascotas_disponibles.html", {"mascotas": mascotas})

@login_required
def detalle_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    return render(request, "mascota/detalle_mascota.html", {"mascota": mascota})

@login_required
def editar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == "POST":
        formulario = Mascota_Form(request.POST, request.FILES, instance=mascota) 
        if formulario.is_valid():
            formulario.save()  
            return redirect('Listar_Mascota')       
    else:
        formulario = Mascota_Form(instance=mascota)
    return render(request, "mascota/editar_mascota.html", {"formulario":formulario , "id": id_mascota})

@login_required
def eliminar_mascota(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    mascota.delete()
    return render(request, "app_proyecto/inicio.html")

#CRUD DE FAVORITOS
@login_required
def listar_favoritos(request):
    favoritos = Mascotas_Favoritas.objects.filter(usuario=request.user) 
    return render(request, "favoritos/listar_favoritos.html", {"favoritos": favoritos})

@login_required
@require_POST
def agregar_favorito(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    Mascotas_Favoritas.objects.create(usuario=request.user, mascota=mascota)
    return redirect('En_Adopcion')

@login_required
def eliminar_favorito(request, id_favorito):
    favorito = Mascotas_Favoritas.objects.get(id=id_favorito)
    favorito.delete()
    return redirect('Listar_Favorito')


# CRUD SOLICITUDES
@login_required
def crear_solicitud(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        formulario = Solicitud_Form(request.POST)
        if formulario.is_valid():
            solicitud = formulario.save(commit=False)
            solicitud.usuario = request.user
            solicitud.mascota = mascota
            solicitud.estado = 'PROCESANDO'
            solicitud.save()
            return redirect('Home')
    else:
        formulario = Solicitud_Form()
    return render(request, 'solicitudes/crear_solicitud.html', {'formulario': formulario})

@login_required
def eliminar_solicitud(request, id_solicitud):
    solicitud = Solicitud_Adopcion.objects.get(id=id_solicitud)
    solicitud.delete()
    return redirect('Listar_Solicitud')

@login_required
def listar_solicitudes(request):
    if request.user.is_superuser: 
        solicitudes = Solicitud_Adopcion.objects.all() 
    else:  
        solicitudes = Solicitud_Adopcion.objects.filter(usuario=request.user)

    return render(request, "solicitudes/listar_solicitudes.html", {"solicitudes": solicitudes})

@login_required
def editar_solicitud(request, id_solicitud):
    solicitud = Solicitud_Adopcion.objects.get(id=id_solicitud)
    if request.method == 'POST':
        formulario = Solicitud_Admin_Form(request.POST, instance=solicitud)
        if formulario.is_valid():
            formulario.save()
            return redirect('Listar_Solicitud')
    else:
        formulario = Solicitud_Admin_Form(instance=solicitud)
    return render(request, 'solicitudes/editar_solicitud.html', {'formulario': formulario})