
from api.v1.views import (ContactUsAPIViev, RateChoicesView, RateViewSet,
                          SourceListAPIView)
from currency.views import *
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

app_name = 'api'
router = DefaultRouter()
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'contacts', ContactUsAPIViev, basename='contacts')

urlpatterns = [
    # path('rates/', RateView.as_view()),
    # path('rates/<int:pk>', RateDeleteView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('rate/choices/', RateChoicesView.as_view(), name='rate-Choices'),
    path('banks/list/', SourceListAPIView.as_view(), name='banks-list'),

]

urlpatterns.extend(router.urls)
