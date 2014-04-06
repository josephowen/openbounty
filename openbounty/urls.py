from django.conf.urls import patterns, url

from openbounty import views, loginviews, profileview, debugviews

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #views.create should eventuallly be in it's own class, like createviews or something
    url(r'^create_challenge', views.create, name='create_challenge'),
    url(r'^view_challenges', views.view_challenges, name='view_challenges'),
    url(r'^challenge/(?P<challenge_id>\d*)', views.challenge, name='challenge'),
    url(r'^login', loginviews.login, name='login'),
    url(r'^register', loginviews.register, name='register'),
    url(r'^logout', loginviews.logout, name='logout'),
    url(r'^profile', profileview.profile, name='profile'),
    url(r'^listusers', debugviews.listusers, name='listusers'),
)
