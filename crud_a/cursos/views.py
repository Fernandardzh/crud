from django.shortcuts import render
from .models import Curso
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class Lista(ListView):
	model=Curso

class Detalle(DetailView):
	model=Curso

class Crear(CreateView):
	model=Curso
	success_url = reverse_lazy('list')
	fields = ['nombre','fecha_inicio','descripcion','imagen']

class Actualiza(UpdateView):
	model=Curso
	success_url = reverse_lazy('list')
	fields= ['nombre','fecha_inicio','descripcion','imagen']	

class Borrale(DeleteView):
	model=Curso
	success_url= reverse_lazy('list')
				