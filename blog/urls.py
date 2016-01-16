from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^a5$', views.post_list),
]