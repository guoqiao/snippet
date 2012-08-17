from django.conf.urls import patterns, url

urlpatterns = patterns('main.views',
    url(r'^$', 'index', name='index'),
    url(r'^new/$', 'new', name='new'),
    url(r'^tags/$', 'tags', name='tags'),
    url(r'^tags/(?P<tag_slug>[^/]+)$', 'tag', name='tag'),
    url(r'^(?P<pk>\d+)/$', 'detail', name='detail'),
)

