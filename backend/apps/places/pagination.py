# apps/hidden_gems/pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # количество объектов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100

