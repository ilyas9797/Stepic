from django.conf.urls import url
from qa.views import test, main_list, popular_list, question, ask, signup, signin, logout_view

app_name = 'qa'
urlpatterns = [
    url(r'^popular/', popular_list, name='popular-list'),
    url(r'^question/(?P<qid>[0-9]+)/$', question, name='question-detail'),
    url(r'^ask/$', ask, name='create-ask'),
    url(r'^$', main_list, name='main-list'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', signin, name='signin'),
    url(r'^logout/$', logout_view, name='logout')
]

