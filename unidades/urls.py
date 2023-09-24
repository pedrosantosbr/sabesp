from django.urls import path
from unidades.views import UnidadeListView

app_name = "unidades"
urlpatterns = [
    path("", UnidadeListView.as_view(), name="index"),
]
