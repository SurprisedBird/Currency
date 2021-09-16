import debug_toolbar
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('currency/', include('currency.urls')),
    path('accounts/', include('accounts.urls')),

    path('auth/', include('django.contrib.auth.urls')),
]
urlpatterns += [url(r'^silk/', include('silk.urls', namespace=' '))]
