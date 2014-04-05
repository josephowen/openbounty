from django.conf.urls import patterns, url

from openbounty import views, loginviews

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #views.create should eventuallly be in it's own class, like createviews or something
    url(r'^create', views.create, name='Create Challenge'),
    url(r'^view_challenges', views.view_challenges, name='View Challenges'),
    url(r'^login', loginviews.login, name='login'),
    url(r'^register', loginviews.register, name='register'),
    url(r'^logout', loginviews.logout, name='logout'),
)
