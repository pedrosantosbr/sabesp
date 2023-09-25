from django.urls import path
from leituras.views import add_leitura, edit_leitura, delete_relatorio

app_name = "leituras"
urlpatterns = [
    path("add", add_leitura, name="add"),
    path("<str:id>/edit", edit_leitura, name="edit"),
    path("<str:id>/delete", delete_relatorio, name="delete"),
]
