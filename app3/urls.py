from django.urls import path
from . import views

app_name='app3'

urlpatterns = [
    path('',views.ingresoUsuario,name='ingresoUsuario'),
    path('informacionUsuario',views.informacionUsuario,name='informacionUsuario'),
    path('consolaAdministrador',views.consolaAdministrador,name='consolaAdministrador'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('ejemploJs',views.ejemploJs,name='ejemploJs'),
    path('devolverDatos',views.devolverDatos,name='devolverDatos'),
    path('devolverAllPubs',views.devolverAllPubs,name='devolverAllPubs'),
    path('devolverPublicacion',views.devolverPublicacion,name='devolverPublicacion'),
    path('publicarComentario',views.publicarComentario,name='publicarComentario'),
    path('crearPublicacion', views.crearPublicacion, name='crearPublicacion'),
    path('inicioReact', views.inicioReact, name='inicioReact')
]
