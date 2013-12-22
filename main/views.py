from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from main.models import Character, Game

def home(request):
	context = RequestContext(request)
	
	character_list = Character.objects.order_by('level')
	game_list = Game.objects.order_by('last_updated')
	context_dict = {'characters':character_list,"games":game_list}
	return render_to_response("home.html", context_dict, context)
