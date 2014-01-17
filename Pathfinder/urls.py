from django.conf.urls import patterns, include, url
from django.conf import settings
from main import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Pathfinder.views.home', name='home'),
    # url(r'^Pathfinder/', include('Pathfinder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^main/', include('main.urls')),

	
    url(r'^$', views.home, name='home'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^player/(?P<player_url>[-\w]+)/$', views.player, name='player'),
    url(r'^create_game/$', views.create_game, name='create_game'),
    url(r'^create_character/$', views.create_character, name='create_character'),
    url(r'^game/(?P<game_url>[-\w]+)/$', views.game, name='game'),
    url(r'^character/(?P<character_url>[-\w]+)/edit/$', views.edit_character, name='edit_character'),
    url(r'^character/(?P<character_url>[-\w]+)/$', views.character, name='character'),
    url(r'^game/(?P<game_url>[-\w]+)/remove/(?P<character_url>[-\w]+)/$', views.remove_character, name='remove_character'),

)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)
