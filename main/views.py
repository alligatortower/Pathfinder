import pdb
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from main.models import Character, Game
from main.forms import UserForm, UserProfileForm, CreateGameForm, CreateCharacterForm, EditGameForm
from datetime import datetime


def home(request):
	context = RequestContext(request, processors=[general_activity_feed])	
	if request.user.is_authenticated():
		character_list = Character.objects.filter(player=request.user)
		my_game_list = Game.objects.filter(gm=request.user)	
		context_dict = {'characters':character_list,"my_games":my_game_list}
	else:
		context_dict = {'characters':None,"my_games":None}

	return render_to_response("home.html", context_dict, context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
	
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')

			else:
				return HttpResponse("Your account is disabled I guess")
		else:
			print "Invalid login deetz: {0},{1}".format(username,password)
			return HttpResponse("invalid login deetz")
	else:
		return render_to_response('login.html', {}, context)

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)

	return HttpResponseRedirect('/')

def register(request):
	context = RequestContext(request)

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			
			new_user = authenticate(username=request.POST['username'],password=request.POST['password'])
			login(request, new_user)
			return HttpResponseRedirect("/")			

		else:
			print user_form.errors,profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
		'register.html',{'user_form':user_form, 'profile_form':profile_form}, context)

def create_game(request):
	context = RequestContext(request)
	if request.method == 'POST':
		create_game_form = CreateGameForm(data=request.POST)
		if create_game_form.is_valid():
			new_game = create_game_form.save(commit=False)
			new_game.gm = request.user
			#new_game.last_updated = datetime.now
			new_game.save()
			return HttpResponseRedirect('/')
		else:
			print create_game_form.errors
	else:
		create_game_form = CreateGameForm()
	return render_to_response(
		'create_game.html',{'create_game_form':create_game_form}, context)

def game(request, game_url):
	context = RequestContext(request)
	game = Game.objects.get(slug=game_url)
	context_dict = {'game':game}

	#if user is gm let him edit the game
	if game.gm == request.user: 
		context_dict.update({'edit_game_form':EditGameForm()})
	
	#figure out what was posted and do that
	if request.method == 'POST': 
		edited_game_form = EditGameForm(data=request.POST)
		if edited_game_form.is_valid():
			cleaned_form_data = edited_game_form.cleaned_data
			character_to_add = cleaned_form_data['character_to_add']
			character_to_add.current_game = game
			character_to_add.save()
			
	character_list = Character.objects.filter(current_game=game)
	context_dict.update({'character_list':character_list})
	return render_to_response(
		'game.html', context_dict, context)

def create_character(request):
	context = RequestContext(request)
	if request.method == 'POST':
		create_character_form = CreateCharacterForm(data=request.POST)
		
		if create_character_form.is_valid():
			new_character = create_character_form.save(commit=False)
			new_character.player = request.user
			new_character.save()
			return HttpResponseRedirect('/')
		else:
			print create_character_form.errors
	else:
		create_character_form = CreateCharacterForm()
	return render_to_response(
		'create_character.html',{'create_character_form':create_character_form}, context)

def remove_character(request, game_url, character_url):
	character_to_remove = Character.objects.get(slug=character_url)
	character_to_remove.current_game = None
	character_to_remove.save()

	return_url = "/game/" + game_url + '/'
	return HttpResponseRedirect(return_url)
		
@login_required
def character(request, character_url):
	context = RequestContext(request)
	character = Character.objects.get(slug=character_url)
	context_dict = {'character':character }
	return render_to_response(
		'character.html', context_dict, context)



#include for the footer box if you want it in that view
def general_activity_feed(request):
	return {
		'general_games' : Game.objects.all()[:5],
		'general_characters' : Character.objects.all()[:5]
	}

	
@login_required
def restricted(request):
	return HttpResponse("You are not logged in, please log in")	
