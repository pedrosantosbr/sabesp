from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound
from rest_framework import status
from alarmes.models import Alarme
from alarmes.api.serializers import AlarmeSerializer
from alarmes.api.pagination import AlarmePagination
from alarmes.api.filters import AlarmeFilter
from rest_framework.response import Response


class AlarmeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alarme.objects.all()
    lookup_field = "id"
    serializer_class = AlarmeSerializer
    filter_backends = (DjangoFilterBackend, AlarmeFilter)
    pagination_class = AlarmePagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        try:
            page = self.paginate_queryset(queryset)
        except NotFound:
            return Response([], status=status.HTTP_200_OK)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            return Response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
