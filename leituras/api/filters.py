from rest_framework import filters


class LeituraFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data = request.query_params.get("data")

        if data:
            queryset = queryset.filter(data_leitura=data)

        return queryset
