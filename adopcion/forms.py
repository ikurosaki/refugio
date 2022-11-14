from django import forms

from .models import Mascota, Persona, Solicitud

class MascotaForm(forms.ModelForm):
    # Contenido de la clase
    class Meta:             
        model = Mascota
        # tupla
        fields = [
            'nombre',
            'sexo',
            'edad_aproximada',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': ' Edad Aproximada',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Personna',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control',}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }

        
class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'apellido',
            'edad',
            'telefono',
            'email',
            'domicilio',
        ]

        label = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'telefono': 'Telefono',
            'email': 'Email',
            'domicilio': 'Domicilio',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.Textarea(attrs={'class':'form-control'}),
        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'numero_mascotas',
            'razones',
        ]

        labels = {
            'numero_mascotas': 'Numero de Mascotas',
            'razones': 'Razones para Adoptar',
        }

        widgets = {
            'numero_mascotas': forms.TextInput(attrs={'class':'form-control'}),
            'razones': forms.Textarea(attrs={'class':'form-control'}),
        }


