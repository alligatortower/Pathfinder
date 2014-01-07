from django import forms
from main.models import UserProfile, Game, Character
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ()

class CreateGameForm(forms.ModelForm):
	name = forms.CharField(max_length=128)
	class Meta:
		model = Game
		fields = ('name',)

class EditGameForm(forms.ModelForm):
	
	class Meta:
		model = Game

class CreateCharacterForm(forms.ModelForm):
	
	class Meta:
		model = Character
		fields = ('name', 'avatar', 'ability_str', 'ability_dex', 'ability_con', 'ability_wis', 'ability_int','ability_cha','hp','base_class_1')
