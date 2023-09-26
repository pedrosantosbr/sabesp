from rest_framework.pagination import PageNumberPagination


class LeituraPagination(PageNumberPagination):
    page_size = 10
    page_query_param = "pagina"
    page_size_query_param = "limite"
    max_page_size = 100
