import pdb
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template.defaultfilters import slugify
from main.models import *
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

def add_character_edit_data(character):	
	data = {}
	data['EditCharacter_Abilities_Form'] = EditCharacter_Abilities_Form(instance=character)
	data['EditCharacter_Details_Form'] = EditCharacter_Details_Form(instance=character)
	data['EditCharacter_Combatstats_Form'] = EditCharacter_Combatstats_Form(instance=character)
	data['EditCharacter_Skills_Form'] = EditCharacter_Skills_Form(instance=character)
	data['add_base_class_form'] = AddBaseClassForm(instance=character)
	data['add_craft_or_profession_form'] = AddCraftOrProfessionForm()
	data['EditMaxRanksForm'] = EditMaxRanksForm(instance=character)
	data['base_classes'] = BaseClass.objects.filter(class_belongs_to=character)
	for value in list(enumerate(data['base_classes'])):
		data['base_classes'][value[0]].__dict__.update({"form": EditBaseClassForm(instance=value[1], prefix=value[0]), "class_number":value[0] })
	data['craft_skills'] = MultiSkill.objects.filter(character=character, sk_craft_or_profession="craft")
	for value in list(enumerate(data['craft_skills'])):   
		data['craft_skills'][value[0]].__dict__.update({"form": EditCraftOrProfessionForm(instance=value[1]), "skill_order":value[0] })
		data['craft_skills'][value[0]].save()
	data['profession_skills'] = MultiSkill.objects.filter(character=character, sk_craft_or_profession="profession")
	for value in list(enumerate(data['profession_skills'])):   
		data['profession_skills'][value[0]].__dict__.update({"form": EditCraftOrProfessionForm(instance=value[1]), "skill_order":value[0]})
		data['profession_skills'][value[0]].save()
	return data
	

@pjax("edit_character_pjax.html")
def character(request, character_url):

	this_character = get_object_or_404(Character, slug=character_url) 
	data = { "character" : this_character }
	if request.method == 'GET' and request.user == this_character.player:
		template = 'edit_character.html'
		data.update(add_character_edit_data(this_character))

	elif request.method == "GET":
		template = 'character.html'
	else:
		return HttpResponse("shit all fucked up")

	return TemplateResponse(request, template, data)

@pjax("edit_character_pjax.html")
def add_base_class(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		form = AddBaseClassForm(request.POST)
		if form.is_valid():
			form_attack_bonus = form.cleaned_data['base_attack_bonus']
			bab_regex = re.findall(r'\+?(\d+)/?', form_attack_bonus)
			form = form.save(commit=False)
			form.class_base_attack_bonus_1 = int(bab_regex[0]) if 0 < len(bab_regex) else 0
			form.class_base_attack_bonus_2 = int(bab_regex[1]) if 1 < len(bab_regex) else 0								
			form.class_base_attack_bonus_3 = int(bab_regex[2]) if 2 < len(bab_regex) else 0
			form.class_base_attack_bonus_4 = int(bab_regex[3]) if 3 < len(bab_regex) else 0
			form.class_belongs_to = this_character
			form.save()
			set_combatstats(this_character)
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)

@pjax("edit_character_pjax.html")
def edit_details(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		form = EditCharacter_Details_Form(data=request.POST, instance=this_character)
		if form.is_valid():
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)


@pjax("edit_character_pjax.html")
def edit_base_class(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		class_name = request.POST['class_name']
		this_class = BaseClass.objects.get(class_belongs_to=this_character, class_name=class_name)
		form = EditBaseClassForm(data=request.POST, instance=this_class)
		if form.is_valid():
			form.save(commit=True)
			set_combatstats(this_character)
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)



@csrf_exempt
@pjax("edit_character_pjax.html")
def delete_base_class(request, character_url):
	print "making it to beginning of view"
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	print "making it to the view"
	if request.method == "POST" and request.user == this_character.player:
		class_to_delete = BaseClass.objects.get(class_belongs_to=this_character, class_name= request.POST['class_name'])
		print class_to_delete.class_name
		class_to_delete.delete()
		data.update(add_character_edit_data(this_character))
		return TemplateResponse(request, "character.html", data)

			

@pjax("edit_character_pjax.html")
def add_multiskill(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		form = AddCraftOrProfessionForm(request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.character = this_character
			form.sk_total = this_character.ability_int_mod + form.sk_ranks + form.sk_misc
			if form.sk_class:
				form.sk_total += 3
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)
		else:
			print form.errors
	else:
		return HttpResonse("You don't have permission to do this")

@pjax("edit_character_pjax.html")
def edit_multiskill(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		skill_domain = request.POST['skill_domain']
		skill_type = request.POST['skill_type']
		skill = MultiSkill.objects.get(character=this_character, sk_domain=skill_domain)
		form = EditCraftOrProfessionForm(data=request.POST, instance=skill)
		if form.is_valid():
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)
		else:
			print form.errors
	else:
		return HttpResonse("You don't have permission to do this")

@csrf_exempt
@pjax("edit_character_pjax.html")
def delete_multiskill(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		skill_domain = request.POST['skill_domain']
		skill = MultiSkill.objects.filter(character=this_character, sk_domain=skill_domain)
		skill.delete()
		data.update(add_character_edit_data(this_character))
		return TemplateResponse(request, "character.html", data)

@pjax("edit_character_pjax.html")
def edit_abilities(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		form = EditCharacter_Abilities_Form(data=request.POST, instance=this_character)
		if form.is_valid():
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)
		else:
			print form.errors
	else:
		return HttpResonse("You don't have permission to do this")

@pjax("edit_character_pjax.html")
def edit_combatstats(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		print "view accepts post"
		form = EditCharacter_Combatstats_Form(data=request.POST, instance=this_character)
		if form.is_valid():
			print "form is valid"
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)
		else:
			print form.errors
	else:
		return HttpResponse("You don't have permission to do this")

@pjax("edit_character_pjax.html")
def edit_skills(request, character_url):
	this_character = get_object_or_404(Character, slug=character_url)
	data = {"character":this_character}
	if request.method == "POST" and request.user == this_character.player:
		if request.POST['which_form'] == "skills_form":
			form = EditCharacter_Skills_Form(data=request.POST, instance=this_character)
		elif request.POST['which_form'] == "max_ranks_form":
			form = EditMaxRanksForm(data=request.POST, instance=this_character)
		if form.is_valid():
			form.save()
			data.update(add_character_edit_data(this_character))
			return TemplateResponse(request, "character.html", data)
		else:
			print form.errors
	else:
		return HttpResonse("You don't have permission to do this")

def remove_character(request, game_url, character_url):
	character_to_remove = Character.objects.get(slug=character_url)
	character_to_remove.current_game = None
	character_to_remove.save()

	return_url = "/game/" + game_url + '/'
	return HttpResponseRedirect(return_url)
		

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
