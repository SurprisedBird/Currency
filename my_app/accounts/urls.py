import django.contrib.auth.urls
from django.conf.urls import url
from django.urls import include, path

from accounts.views import MyProfileView

app_name = 'accounts'

urlpatterns = [
    path('my-profile/', MyProfileView.as_view(), name='my-profile'),
    url('^', include('django.contrib.auth.urls')),
]
