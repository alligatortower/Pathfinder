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
		fields = ('name', 'avatar', 'ability_str_base', "ability_dex_base", 'ability_con_base', 'ability_wis_base', 'ability_int_base','ability_cha_base','hp','base_class_1')

class EditCharacter_Abilities_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ('ability_str_base', 'ability_dex_base', 'ability_con_base', 'ability_wis_base', 'ability_int_base','ability_cha_base')

	def save(self,commit=True, *args, **kwargs):
		instance = super(EditCharacter_Abilities_Form, self).save(commit=False)
		if commit:
			set_abilities(instance)
			instance.save()
		return instance

class EditCharacter_Combatstats_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ('hp','bab','ac')
	
def set_abilities(instance):		
	instance.ability_str_score = instance.ability_str_base + instance.ability_str_temp
	instance.ability_str_mod = (instance.ability_str_score - 10) / 2
	instance.ability_dex_score = instance.ability_dex_base + instance.ability_dex_temp
	instance.ability_dex_mod = (instance.ability_dex_score - 10) / 2
	instance.ability_con_score = instance.ability_con_base + instance.ability_con_temp
	instance.ability_con_mod = (instance.ability_con_score - 10) / 2
	instance.ability_int_score = instance.ability_int_base + instance.ability_int_temp
	instance.ability_int_mod = (instance.ability_int_score - 10) / 2
	instance.ability_wis_score = instance.ability_wis_base + instance.ability_wis_temp
	instance.ability_wis_mod = (instance.ability_wis_score - 10) / 2
	instance.ability_cha_score = instance.ability_cha_base + instance.ability_cha_temp
	instance.ability_cha_mod = (instance.ability_cha_score - 10) / 2
