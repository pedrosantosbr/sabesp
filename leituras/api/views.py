from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from leituras.models import Leitura
from leituras.api.serializers import LeituraSerializer
from leituras.api.pagination import LeituraPagination
from leituras.api.filters import LeituraFilter
from rest_framework.response import Response


class LeituraReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leitura.objects.all()
    lookup_field = "id"
    serializer_class = LeituraSerializer
    filter_backends = (DjangoFilterBackend, LeituraFilter)
    pagination_class = LeituraPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # return self.get_paginated_response(serializer.data)
            return Response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
