
from django.urls import path

from currency.views import *

app_name = 'currency'

urlpatterns = [
    path('contactus/', get_contact_us),

    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', CreateRateViev.as_view(), name='create-rate'),
    path('rate/details/<int:pk>/', DetailRateView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', UpdateRateView.as_view(), name='update-rate'),
    path('rate/delete/<int:pk>/', DeleteRateView.as_view(), name='delete-rate'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', CreateSourseViev.as_view(), name='create-source'),
    path('source/details/<int:pk>/', DetailSourseView.as_view(), name='source-details'),
    path('source/update/<int:pk>/', UpdateSourseView.as_view(), name='update-source'),
    path('source/delete/<int:pk>/', DeleteSorceView.as_view(), name='delete-source'),
    path('contactus/create/', ContactUsCreateViev.as_view(), name='contactus-create')
]
