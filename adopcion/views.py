from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from adopcion.forms import MascotaForm, PersonaForm, SolicitudForm

from .models import Mascota, Solicitud, Persona


# Importando Vista Basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

from django.urls import reverse_lazy



# Create your views here.
 
def index(request):
    return render(request, 'adopcion/index.html')

# Views del Forms
"""
def form(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')
    else:  
        form = MascotaForm()
        
    return render(request, 'adopcion/form.html', {'form': form })
    """

# Views del List
"""
def list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas': mascota}
    
    return render(request, 'adopcion/list.html', contexto)
"""

# Vista para Editar
def edit(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'adopcion/form.html', {'form': form})


# Vista para Borrar
def delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('list')
    return render(request, 'adopcion/delete.html', {'mascota': mascota})
    

# Vistas basadas en Clases

# Views del List
class List(ListView):  
    model = Mascota
    template_name = 'adopcion/list.html'


class Form(CreateView):
    model = Mascota
    form_class = MascotaForm 
    template_name = 'adopcion/form.html'
    success_url = reverse_lazy('list')


class Edit(UpdateView):
    model = Mascota
    form_class = MascotaForm 
    template_name = 'adopcion/form.html'
    success_url = reverse_lazy('list')


class Delete(DeleteView):
    model = Mascota
    template_name = 'adopcion/delete.html'
    success_url = reverse_lazy('list')


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'


# En esta vista estamos usando 2 formularios
class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    
    success_url = reverse_lazy('solicitud_list')

    def get_context_data(self, **kwargs):
        # Crear contexto
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
       
        # Form 1 , Mandar formuladios a la Calse
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)

        # Formulario 2
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        return context
    

    # Metodo POST
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_ur())
        else: 
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

    
           



