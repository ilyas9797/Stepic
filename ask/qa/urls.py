from django.conf.urls import url
from qa.views import test, main_list, popular_list, question, ask

app_name = 'qa'
urlpatterns = [
    url(r'^popular/', popular_list, name = 'popular-list'),
    url(r'^question/(?P<qid>[0-9]+)/$', question, name = 'question-detail'),
    url(r'^ask/$', ask, name='create-ask'),
    url(r'^$', main_list, name = 'main-list'),
]
