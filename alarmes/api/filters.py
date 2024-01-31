from rest_framework import filters
from rest_framework.exceptions import ValidationError


class AlarmeFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data, page, limit = (
            request.query_params.get("data"),
            request.query_params.get("pagina"),
            request.query_params.get("limite"),
        )

        if not data or data == "":
            raise ValidationError(detail="O parâmetro data é obrigatório.")
        if not page or page == "":
            raise ValidationError(detail="O parâmetro pagina é obrigatório.")
        if not limit or limit == "":
            raise ValidationError(detail="O parâmetro limite é obrigatório.")
        if data:
            queryset = queryset.filter(data=data)

        return queryset
