from django.urls import path

# from apps.adopcion.views import index
from . import views

app_name = 'adopcion'
# urlpatterns = [
#     path('', index),
# ]

urlpatterns = [
    path('', views.index, name='index'),
]
