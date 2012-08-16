from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'detail', name='detail'),
)

