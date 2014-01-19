from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from main.models import UserProfile, Game, Character

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

class EditGameForm(forms.Form):
	character_to_add = forms.ModelChoiceField(queryset = Character.objects.filter(current_game=None))
	
	def clean_chracter_to_add(self):
		character_name = self.cleaned_data['character_to_add']
		character = Character.objects.get(name=character_name)
		return character

	class Meta:
		fields = ('characters',)

class CreateCharacterForm(forms.ModelForm):
	
	class Meta:
		model = Character
		fields = ('name', 'avatar', 'ability_str', 'ability_dex', 'ability_con', 'ability_wis', 'ability_int','ability_cha','hp','base_class_1')

class EditCharacter_Abilities_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ('ability_str', 'ability_dex', 'ability_con', 'ability_wis', 'ability_int','ability_cha')

class EditCharacter_Combatstats_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ('hp','bab','ac')
