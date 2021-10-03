import rest_framework
from api.v1.filters import ContactUsFilter, RateFilter
from api.v1.paginators import RatePagination
from api.v1.serializers import (ContactUsSerializer, RateSerializer,
                                SourceSerializer)
from api.v1.throttles import AnonUserRateThrottle
from currency import model_choices
from currency.models import ContactUs, Rate, Source
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework import generics, serializers, viewsets
from rest_framework.response import Response

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


class RateChoicesView(generics.GenericAPIView):
    def get(self, reuest):
        return Response({'rate_types': model_choices.RATE_TYPES})


class SourceListAPIView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = RatePagination


class ContactUsAPIViev(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    pagination_class = RatePagination
    filter_class = ContactUsFilter
    filter_backends = (filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter,
                       rest_framework_filters.SearchFilter)
    ordering_fields = ['id', 'created', 'email_to', 'subject']
    search_fields = ['email_to', 'subject']
    throttle_classes = [AnonUserRateThrottle]

    read_only_fields = ['created']
