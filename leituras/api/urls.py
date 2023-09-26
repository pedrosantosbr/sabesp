from django.urls import path
from leituras.api.views import LeituraReadOnlyViewSet

urlpatterns = [
    path("", LeituraReadOnlyViewSet.as_view({"get": "list"}), name="leituras-read"),
]
