from django.conf.urls import include, url, patterns
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'webdev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^accounts/', include('allauth.urls')),
    url(r'^login/', include('social_auth.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include('myapp.urls')),
]