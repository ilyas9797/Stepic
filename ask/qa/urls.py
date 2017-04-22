from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^(?P<id>[0-9]+)/$', test, name = 'test'),
]
