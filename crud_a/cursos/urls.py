from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',
		views.Lista.as_view(),
		name='list'),

	url(r'^(?P<pk>\d+)$',
		views.Detalle.as_view(),
		name='detail'),

	url(r'^nuevo/$',
		views.Crear.as_view(),
		name='new'),

	url(r'^editar/(?P<pk>\d+)$',
		views.Actualiza.as_view(),
		name='edit'),

	url(r'^borrar/(?P<pk>\d+)$',
		views.Borrale.as_view(),
		name='delete'),




]