from django.urls import path

from apps.adopcion.views import index

app_name = 'adopcion'
urlpatterns = [
    path('', index),
]
