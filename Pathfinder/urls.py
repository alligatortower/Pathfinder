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
    url(r'^character/(?P<character_url>[-\w]+)/edit_abilities/$', views.edit_abilities, name='edit_abilities'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_combatstats/$', views.edit_combatstats, name='edit_combatstats'),
    url(r'^character/(?P<character_url>[-\w]+)/add_base_class/$', views.add_base_class, name='add_base_class'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_base_class/$', views.edit_base_class, name='edit_base_class'),
    url(r'^character/(?P<character_url>[-\w]+)/delete_base_class/$', views.delete_base_class, name='delete_base_class'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_details/$', views.edit_details, name='edit_details'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_health/$', views.edit_health, name='edit_health'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_initiative/$', views.edit_initiative, name='edit_initiative'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_ac/$', views.edit_ac, name='edit_ac'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_speed/$', views.edit_speed, name='edit_speed'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_base_attack/$', views.edit_base_attack, name='edit_base_attack'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_combat_maneuvers/$', views.edit_combat_maneuvers, name='edit_combat_maneuvers'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_saves/$', views.edit_saves, name='edit_saves'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_skills/$', views.edit_skills, name='edit_skills'),
    url(r'^character/(?P<character_url>[-\w]+)/edit_multiskill/$', views.edit_multiskill, name='edit_multiskill'),
    url(r'^character/(?P<character_url>[-\w]+)/add_multiskill/$', views.add_multiskill, name='add_multiskill'),
    url(r'^character/(?P<character_url>[-\w]+)/delete_multiskill/$', views.delete_multiskill, name='delete_multiskill'),
    url(r'^character/(?P<character_url>[-\w]+)/$', views.character, name='character'),
    url(r'^game/(?P<game_url>[-\w]+)/remove/(?P<character_url>[-\w]+)/$', views.remove_character, name='remove_character'),
    url(r'^what_to_create/(?P<what_is_making>[-\w]+)/(?P<who_is_making>[-\w]+)/$', views.WhatToCreate, name='WhatToCreate'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)
