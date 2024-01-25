from django.urls import path
from alarmes.api.views import index

app_name = "alarmes"
urlpatterns = [
    path("", index, name="index"),
]
