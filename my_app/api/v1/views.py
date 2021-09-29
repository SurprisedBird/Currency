from api.v1.filters import RateFilter
from api.v1.paginators import RatePagination
from api.v1.serializers import RateSerializer
from api.v1.throttles import AnonUserRateThrottle
from currency.models import Rate
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework import viewsets

# class RateView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


# class RateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().select_related('source')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filter_class = RateFilter
    filter_backends = (filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter,)
    ordering_fields = ['id', 'created', 'sale', 'buy']
    throttle_classes = [AnonUserRateThrottle]
