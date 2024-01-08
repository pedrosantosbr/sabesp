from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static


# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )

from oauth.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    # dashboard
    path("", include("dashboard.urls")),
    path(
        "leituras/",
        include(
            "leituras.urls",
            namespace="leituras",
        ),
    ),
    path(
        "unidades/",
        include(
            "unidades.urls",
            namespace="unidades",
        ),
    ),
    # api
    path("api/v1/leituras", include("leituras.api.urls")),
    # jwt
    path("api/v1/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/v1/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
