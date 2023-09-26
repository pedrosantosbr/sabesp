from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from leituras.models import Leitura
from leituras.api.serializers import LeituraSerializer
from leituras.api.pagination import LeituraPagination
from leituras.api.filters import LeituraFilter


class LeituraReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leitura.objects.all()
    lookup_field = "id"
    serializer_class = LeituraSerializer
    filter_backends = (DjangoFilterBackend, LeituraFilter)
    pagination_class = LeituraPagination
