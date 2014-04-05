from django.conf.urls import patterns, url

from openbounty import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
