from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/efreiAPI$', views.Livre_list_published),
    url(r'^api/addEfreiAPI$', views.add_livre),
    url(r'^api/efreiAPI/(?P<pk>[0-9]+)$', views.delete_livre),
]