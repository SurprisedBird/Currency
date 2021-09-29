
from api.v1.views import RateViewSet
from currency.views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = 'api'
router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')

urlpatterns = [
    # path('rates/', RateView.as_view()),
    # path('rates/<int:pk>', RateDeleteView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns.extend(router.urls)
