from django.urls import include, path, re_path

from . import views 

#from django.views.generic import TemplateView
#from django.views.generic import ListView, CreateView, UpdateView,



urlpatterns = [
    path('', views.index, name='index'),
    #path('form', views.form, name='form'),
    #path('list', views.list, name='list'),

    # URL Vista basada en Clases
    path('list', views.List.as_view(), name='list'),
    path('form', views.Form.as_view(), name='form'),
    path('solicitudlist', views.SolicitudList.as_view(), name='solicitudlist'),
    path('solicitudcreate', views.SolicitudCreate.as_view(), name='solicitudcreate'),


    # Regular expresion (Lo que cambia es lo que pasamos o recibimos, lo que vamos a recibir en la barra de Direcciones)

    #forma 1 EDITAR (Metodo mas viejo) vista basada en funciones
    #re_path(r'^edit/(?P<id_mascota>\d+)/$', views.edit, name='edit'),

    #forma 2 EDITAR vista basada en funciones
    #path('edit/<int:id_mascota>/', views.edit, name='edit'),

    #forma 3 EDITAR vista basada en Clases
    path('edit/<int:pk>/', views.Edit.as_view(), name='edit'),

    #forma DELETE vista basada en Funciones
    #path('delete/<int:id_mascota>/', views.Delete, name='delete'),

    #forma DELETE vista basada en Clases
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]