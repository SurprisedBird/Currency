
from api.v1.views import RateViewSet
from currency.views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')

urlpatterns = [
    # path('rates/', RateView.as_view()),
    # path('rates/<int:pk>', RateDeleteView.as_view()),

]

urlpatterns.extend(router.urls)
