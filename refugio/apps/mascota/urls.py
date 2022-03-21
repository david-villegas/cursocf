from django.urls import path
from django.contrib.auth.decorators import login_required

# from apps.mascota.views import index,mascota_view, mascota_list
from . import views

app_name = 'mascota'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('nuevo', views.mascota_view, name='mascota_crear'),
#     path('listar', views.mascota_list, name='mascota_listar'),
#     path('editar/<id_mascota>', views.mascota_edit, name='mascota_editar'),
#     path('eliminar/<id_mascota>', views.mascota_delete, name='mascota_eliminar'),
# ]

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', login_required(views.MascotaCreate.as_view()), name='mascota_crear'),
    path('listar', login_required(views.MascotaList.as_view()), name='mascota_listar'),
    path('editar/<pk>', login_required(views.MascotaUpdate.as_view()), name='mascota_editar'),
    path('eliminar/<pk>', login_required(views.MascotaDelete.as_view()), name='mascota_eliminar'),
    path('listado', views.listadousuarios, name='listado'),
]
