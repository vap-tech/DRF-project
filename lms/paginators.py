from rest_framework.pagination import PageNumberPagination


class LmsPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
