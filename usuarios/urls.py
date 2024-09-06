from django.urls import path # type: ignore
from usuarios.views import login, cadastro # type: ignore

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
]
