from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    url(r'^$', 'home', name='home'),
    url(r'^logout/$', 'logout_user', name='logout'),
    url(r'^register/$', 'register', name='register'),
)

urlpatterns += patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login',{'template_name': 'accounts/login.html'}, name='login'),
)

