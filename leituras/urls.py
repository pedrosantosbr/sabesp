from django.urls import path
from leituras.views import add_leitura

app_name = "leituras"
urlpatterns = [
    path("add", add_leitura, name="add"),
]
