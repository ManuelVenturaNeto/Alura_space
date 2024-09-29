from django.urls import path # type: ignore
from usuarios.views import login, cadastro, logout # type: ignore

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
]
