from django.urls import path

# from apps.adopcion.views import index
from . import views

app_name = 'adopcion'
urlpatterns = [
    path('', views.index, name='index'),
    path('solicitud/listar',views.SolicitudList.as_view(), name='solicitud_listar'),
    path('solicitud/nueva',views.SolicitudCreate.as_view(), name='solicitud_crear'),
]
