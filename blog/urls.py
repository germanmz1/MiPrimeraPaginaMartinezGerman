from django.urls import path
from .views import inicio, crear_post, buscar_post

urlpatterns = [
    path('', inicio, name='inicio'),
    path('crear/', crear_post, name='crear_post'),
    path('buscar/', buscar_post, name='buscar_post'),
]