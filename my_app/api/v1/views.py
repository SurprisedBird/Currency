from api.v1.paginators import RatePagination
from api.v1.serializers import RateSerializer
from currency.models import Rate
from rest_framework import viewsets

# class RateView(generics.ListCreateAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer


# class RateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer

class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = RatePagination
