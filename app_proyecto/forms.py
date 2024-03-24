from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar, Raza, Mascota, Solicitud_Adopcion


# FORMULARIOS PARA EL USER (REGISTRO Y EDICION)
class Usuario_Registro(UserCreationForm):
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Nombre usuario', help_text=None)
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text=None)
    password2 = forms.CharField(label='Repetir Password',widget=forms.PasswordInput, help_text=None)

    class Meta:
        model = User
        fields = ["username", "email", "first_name","last_name","password1","password2"]
        

class Usuario_Editar_Perfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    imagen= forms.ImageField(required=False, label='Avatar',widget=forms.ClearableFileInput(attrs={'multiple': False}))
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "imagen"]

# FORMULARIO PARA LA RAZA
class Raza_Form(forms.Form):
    nombre = forms.CharField(max_length=100)
    origen = forms.CharField(max_length=100)
    tamanio_promedio = forms.CharField(max_length=50)
    esperanza_de_vida = forms.IntegerField()
    descripcion = forms.CharField(max_length=200)

# FORMULARIO PARA LA MASCOTA
class Mascota_Form(forms.ModelForm):
    TIPO = [('PERRO', 'Perro'),('GATO', 'Gato'),('OTRO', 'Otro'),]
    nombre = forms.CharField(max_length=50)
    raza = forms.ModelChoiceField(queryset=Raza.objects.all())
    tipo = forms.ChoiceField(choices=TIPO)
    descripcion = forms.CharField(widget=forms.Textarea)
    foto = forms.ImageField(required=False)
    disponible = forms.BooleanField(initial=True, required=False)
    class Meta:
        model = Mascota
        fields = '__all__'

class Solicitud_Form(forms.ModelForm):
    class Meta:
        model = Solicitud_Adopcion
        fields = ['mensaje']

class Solicitud_Admin_Form(forms.ModelForm):
    class Meta:
        model = Solicitud_Adopcion
        fields = ['respuesta','estado']
    