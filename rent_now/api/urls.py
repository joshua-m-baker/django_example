from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.hello_world, name='hello_world'),
]