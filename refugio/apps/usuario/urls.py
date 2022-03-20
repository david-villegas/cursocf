from django.urls import path

from . import views

app_name = 'usuario'
urlpatterns = [
    path('registrar/', views.RegistroUsuario.as_view(), name='registrar'),
]
