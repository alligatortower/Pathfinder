import pdb
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template.defaultfilters import slugify
from main.models import Character, Game, UserProfile, User
from main.forms import *
from datetime import datetime
from djpjax import pjax

def home(request):
	context = RequestContext(request)	
	context_dict=	{'general_games' : Game.objects.all().order_by("-last_updated")[:5],
			'general_characters' : Character.objects.all().order_by("-created")[:5]}

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

def player(request,player_url):
	context = RequestContext(request)
	
	this_player = User.objects.get(username=player_url)
	player_games = Game.objects.filter(gm=this_player)
	player_characters = Character.objects.filter(player=this_player)
	
	context_dict = {"player_games":player_games, "player_characters":player_characters, "this_player":this_player}	
	
	return render_to_response(
		'player.html', context_dict, context)

@login_required
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
	game = Game.objects.get(slug=game_url)
	data = {'game':game}

	#if user is gm let him edit the game
	if game.gm == request.user: 
		data['edit_game_form'] = EditGameForm()
	
	#figure out what was posted and do that
	if request.method == 'POST': 
		edited_game_form = EditGameForm(data=request.POST)
		if edited_game_form.is_valid():
			cleaned_form_data = edited_game_form.cleaned_data
			character_to_add = cleaned_form_data['character_to_add']
			character_to_add.current_game = game
			character_to_add.save()
			game.save() #to update last_updated
			
	character_list = Character.objects.filter(current_game=game)
	data['character_list'] = character_list
	return render(request, 'game.html', data)

@login_required
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

@pjax("edit_character_pjax.html")
def EditCharacter(request, character_url):
	data = {}
	this_character = get_object_or_404(Character, slug=character_url)
	if request.method == 'GET' and request.user == this_character.player:
		template = 'edit_character.html'
		data['EditCharacter_Abilities_Form'] = EditCharacter_Abilities_Form(instance=this_character)
		data['EditCharacter_Combatstats_Form'] = EditCharacter_Combatstats_Form(instance=this_character)

	elif request.method == 'POST':
		if request.POST['tab'] == "ability_tab":
			edit_character_form = EditCharacter_Abilities_Form(request.POST, instance=this_character)
		elif request.POST['tab'] == "combatstats_tab":
			edit_character_form = EditCharacter_Combatstats_Form(request.POST, instance=this_character)
		else:
			return HttpResponse("No Tab")		

		if edit_character_form.is_valid():
			edit_character_form.save()
			data["character"] = this_character
			data['EditCharacter_Abilities_Form'] = EditCharacter_Abilities_Form(instance=this_character)
			data['EditCharacter_Combatstats_Form'] = EditCharacter_Combatstats_Form(instance=this_character)
			
		else:
			print edit_character_form.errors
			return HttpResponse("badSumbit")
	elif request.method == "GET":
		template = 'character.html'
	else:
		return HttpResponse("shit all fucked up")

	return TemplateResponse(request, template, data)

def remove_character(request, game_url, character_url):
	character_to_remove = Character.objects.get(slug=character_url)
	character_to_remove.current_game = None
	character_to_remove.save()

	return_url = "/game/" + game_url + '/'
	return HttpResponseRedirect(return_url)
		
@login_required
@ensure_csrf_cookie
def character(request, character_url):
	character = get_object_or_404(Character, slug=character_url)
	data = {'character':character }

	if request.user == character.player:
		template_name = 'edit_character.html'
		data['EditCharacter_Abilities_Form'] = EditCharacter_Abilities_Form(instance=character)
		data['EditCharacter_Combatstats_Form'] = EditCharacter_Combatstats_Form(instance=character)
		data['EditCharacter_Skills_Form'] = EditCharacter_Skills_Form(instance=character)

	else:
		template_name = 'character.html'
	return TemplateResponse(request, template_name, data)

def WhatToCreate(request, what_is_making, who_is_making):
	data = {}
	character = False
	game = False
	if what_is_making == "character":
		character = get_object_or_404(Character, slug=who_is_making)
		if not request.user == character.player:
			return HttpResponse("only the player controlling the character can do this")
		data['character'] = character
	elif what_is_making == "game":
		game = get_object_or_404(Game, slug=who_is_making)
		if not request.user == game.gm:
			return HttpResponse("Only game GM can do this")
		data['game'] = game
	else:
		return HttpResponse("view is failing, this is not being created by a game or character")

	if request.method == "GET":
		data['WhatToCreateForm'] = WhatToCreateForm()
		template = "what_to_create.html"
	elif request.method == "POST":
		form = WhatToCreateForm(data=request.POST)
		if form.is_valid():
			if request.POST['what'] == "Armor":
				data['item_to_create'] = CreateArmorForm()
			elif request.POST['what'] == "Weapon":
				data['item_to_create'] = CreateWeaponForm()
			template = "create_armor_or_weapon.html"
	else:
		return HttpResponse("Something fuckd up")

	return render(request, template, data)


	
@login_required
def restricted(request):
	return HttpResponse("You are not logged in, please log in")	
