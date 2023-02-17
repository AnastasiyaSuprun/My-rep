from rest_framework.pagination import PageNumberPagination


class OwnerPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 100


class PetPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100


class ShelterPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'page_size'
    max_page_size = 100
