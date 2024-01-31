from django.urls import path
from alarmes.api.views import AlarmeViewSet

app_name = "alarmes"
urlpatterns = [
    path("", AlarmeViewSet.as_view({"get": "list"}), name="alarmes"),
]
