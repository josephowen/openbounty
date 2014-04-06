from django.conf.urls import patterns, url

from openbounty import views, loginviews, profileview, debugviews

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #views.create should eventuallly be in it's own class, like createviews or something
    url(r'^create_bounty', views.create, name='create_bounty'),
    url(r'^view_bounties', views.view_challenges, name='view_bounties'),
    url(r'^bounty/(?P<challenge_id>\d*)', views.challenge, name='bounty'),
    url(r'^login', loginviews.login, name='login'),
    url(r'^register', loginviews.register, name='register'),
    url(r'^logout', loginviews.logout, name='logout'),
    url(r'^profile', profileview.profile, name='profile'),
    url(r'^listusers', debugviews.listusers, name='listusers'),
)
