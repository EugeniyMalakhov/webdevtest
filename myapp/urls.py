from django.conf.urls import url, include

urlpatterns = [
    #url(r'^login/$', 'myapp.views.login', name='login'),
    #url(r'^accounts/profile/oauth2callback/', 'myapp.views.home', name='home'),
    url(r'^logout/$', 'myapp.views.logout', name='logout'),
    url(r'^accounts/profile/', 'myapp.views.home', name='home'),
    url(r'^accounts/login/complete/odnoklassniki/', 'myapp.views.home', name='home'),
    url(r'^article/(?P<articles_id>\d+)/$', 'myapp.views.article', name='article'),
    url(r'^article/addarticle/(?P<user_id>\d+)/$', 'myapp.views.addarticle', name='addarticle'),
    url(r'^article/deleteart/(?P<articles_id>\d+)/$', 'myapp.views.article_delete', name='deletearticle'),
    url(r'^comment/deletecomm/(?P<articles_id>\d+)/(?P<comment_id>\d+)/$', 'myapp.views.comment_delete', name='deletearticle'),
    url(r'^comment/deletesub/(?P<articles_id>\d+)/(?P<subcomment_id>\d+)/$', 'myapp.views.subcomment_delete', name='deletearticle'),
    url(r'^article/addcomment/(?P<articles_id>\d+)/(?P<user_id>\d+)/$', 'myapp.views.addcomment', name='addcomment'),
    url(r'^comment/addsubcomment/(?P<articles_id>\d+)/(?P<comment_id>\d+)/(?P<user_id>\d+)/$', 'myapp.views.addsubcomment', name='addsubcomment'),
    url(r'^page/(\d+)/$', 'myapp.views.home'),
    url(r'^$', 'myapp.views.home', name='home'),
]
