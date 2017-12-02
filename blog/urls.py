from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='the_wandering_marta'),
]