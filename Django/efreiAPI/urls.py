from django.conf.urls import url
from livre import views

urlpatterns = [
    url(r'^api/livres$', views.livre_list),
    url(r'^api/livres/(?P<pk>[0-9]+)$', views.livre_detail),
    url(r'^api/livres/published$', views.livre_list_published)
]