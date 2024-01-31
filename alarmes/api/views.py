from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from alarmes.models import Alarme
from alarmes.api.serializers import AlarmeSerializer
from alarmes.api.pagination import AlarmePagination
from alarmes.api.filters import AlarmeFilter


class AlarmeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alarme.objects.all()
    lookup_field = "id"
    serializer_class = AlarmeSerializer
    filter_backends = (DjangoFilterBackend, AlarmeFilter)
    pagination_class = AlarmePagination
