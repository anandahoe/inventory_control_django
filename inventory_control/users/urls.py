from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("usuarios/", views.index, name="index"),
    path("usuarios/cadastro/", views.create, name="create"),
    path("login/", views.login, name="login"),
    path("usuarios/<str:username>", views.update, name="update"),
    path("usuarios/<int:id>/delete", views.delete, name="delete"),
    path("logout/", views.logout, name="logout")
]