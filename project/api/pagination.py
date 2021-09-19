from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination ,CursorPagination

class watchListPNPagnation(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param ='size'
    max_page_size = 1
    last_page_strings = 'end' #defualt ==> last

class watchListLOPagnation(LimitOffsetPagination):
    default_limit = 2
    limit_query_param= 'lm'
    offset_query_param ='po'
    max_limit = 3
  
class watchListCRPagnation(CursorPagination):
    page_size = 2
    cursor_query_param = 'next'
    ordering ='created'
    