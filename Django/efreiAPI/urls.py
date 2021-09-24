<<<<<<< HEAD
<<<<<<< HEAD
=======
from django.urls import path
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^api/livres$', views.livre_list),
    url(r'^api/livres/(?P<pk>[0-9]+)$', views.livre_detail),
    url(r'^api/livres/published$', views.livre_list_published)
=======
from django.urls import path
from django.conf.urls import url 
from . import views

urlpatterns = [
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
    url(r'^api/efreiAPI$', views.Livre_list_published),
    url(r'^api/addEfreiAPI$', views.add_livre),
    url(r'^api/efreiAPI/(?P<pk>[0-9]+)$', views.delete_livre),
    url(r'^api/PutEfreiAPI/(?P<pk>[0-9]+)$', views.update_livre),
<<<<<<< HEAD
>>>>>>> pull
=======
>>>>>>> 49fd3c8b311a0d8a1bb0c12fff3851f63259fc89
]