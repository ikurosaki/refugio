from django.contrib import admin

from .models import Persona, Mascota, Vacuna

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

admin.site.register(Persona, PersonaAdmin)


class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',)

admin.site.register(Mascota, MascotaAdmin)


class VacunaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Vacuna, VacunaAdmin)
