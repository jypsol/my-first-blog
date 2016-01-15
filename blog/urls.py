from django.conf.urls import include, url
from blog.views import archive

    urlpatterns = patterns('',
        url(r'^$', archive),
    )