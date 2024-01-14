from rest_framework.generics import ListAPIView, ListCreateAPIView
from pagination import MyPagination

class MyListAPIView(ListAPIView):
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        if 'all' in self.request.query_params:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    

class MyListCreateAPIView(ListCreateAPIView):
    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        if 'all' in self.request.query_params:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    
    def get_queryset(self):
        if 'all' in self.request.query_params:
            return self.queryset
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)