from django.urls import path
from leituras.api.views import get_leituras

urlpatterns = [
    path("", get_leituras, name="list"),
]
