from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from main.models import Character, Game
from main.forms import UserForm, UserProfileForm

def home(request):
	context = RequestContext(request)
	
	character_list = Character.objects.order_by('level')
	game_list = Game.objects.order_by('last_updated')
	context_dict = {'characters':character_list,"games":game_list}

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
	registered = False

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

			registered = True

		else:
			print user_form.errors,profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
		'register.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered}, context)
