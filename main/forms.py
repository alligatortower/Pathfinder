import pdb
from django import forms
from django.db.models import Q
from django.contrib.auth.models import User
from main.models import *

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
			set_combatstats(instance)
			set_skills(instance)
			instance.save()
		return instance

class EditCharacter_Combatstats_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ('hp','bab','ac')

class AddWeaponForm(forms.ModelForm):
	
	class Meta:
		model = Weapon
		exclude = ("owner","current_game","is_equiped")



	
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

def set_combatstats(instance):
	instance.initiative = instance.ability_dex_mod + instance.initiative_misc
	instance.ac = instance.ability_dex_mod + instance.ac_armor + instance.ac_shield + instance.ac_natural + instance.ac_misc
	instance.cmb = instance.bab + instance.ability_str_mod # + instance.size_mod

def set_skills(instance):
	instance.sk_acrobatics = instance.ability_dex_mod + instance.sk_acrobatics_ranks + instance.sk_acrobatics_misc - instance.armor_check_penalty
	if instance.sk_acrobatics_class:
		instance.sk_acrobatics += 3
	instance.sk_appraise = instance.ability_int_mod + instance.sk_appraise_ranks + instance.sk_appraise_misc
	if instance.sk_appraise_class:
		instance.sk_appraise += 3
	instance.sk_bluff = instance.ability_cha_mod + instance.sk_bluff_ranks + instance.sk_bluff_misc
	if instance.sk_bluff_class:
		instance.sk_bluff += 3
	instance.sk_climb = instance.ability_str_mod + instance.sk_climb_ranks + instance.sk_climb_misc - instance.armor_check_penalty
	if instance.sk_climb_class:
		instance.sk_climb += 3
	instance.sk_craft = instance.ability_int_mod + instance.sk_craft_ranks + instance.sk_craft_misc
	if instance.sk_craft_class:
		instance.sk_craft += 3
	instance.sk_diplomacy = instance.ability_cha_mod + instance.sk_diplomacy_ranks + instance.sk_diplomacy_misc
	if instance.sk_diplomacy_class:
		instance.sk_diplomacy += 3
	instance.sk_disable_device = instance.ability_dex_mod + instance.sk_disable_device_ranks + instance.sk_disable_device_misc - instance.armor_check_penalty
	if instance.sk_disable_device_class:
		instance.sk_disable_device += 3
	instance.sk_disguise = instance.ability_cha_mod + instance.sk_disguise_ranks + instance.sk_disguise_misc
	if instance.sk_disguise_class:
		instance.sk_disguise += 3
	instance.sk_escape_artist = instance.ability_dex_mod + instance.sk_escape_artist_ranks + instance.sk_escape_artist_misc - instance.armor_check_penalty
	if instance.sk_escape_artist_class:
		instance.sk_escape_artist += 3
	instance.sk_fly = instance.ability_dex_mod + instance.sk_fly_ranks + instance.sk_fly_misc - instance.armor_check_penalty
	if instance.sk_fly_class:
		instance.sk_fly += 3
	instance.sk_handle_animal = instance.ability_cha_mod + instance.sk_handle_animal_ranks + instance.sk_handle_animal_misc
	if instance.sk_handle_animal_class:
		instance.sk_handle_animal += 3
	instance.sk_heal = instance.ability_wis_mod + instance.sk_heal_ranks + instance.sk_heal_misc
	if instance.sk_heal_class:
		instance.sk_heal += 3
	instance.sk_intimidate = instance.ability_cha_mod + instance.sk_intimidate_ranks + instance.sk_intimidate_misc
	if instance.sk_intimidate_class:
		instance.sk_intimidate += 3
	instance.sk_knowledge_arcana = instance.ability_int_mod + instance.sk_knowledge_arcana_ranks + instance.sk_knowledge_arcana_misc
	if instance.sk_knowledge_arcana_class:
		instance.sk_knowledge_arcana += 3
	instance.sk_knowledge_dungeoneering = instance.ability_int_mod + instance.sk_knowledge_dungeoneering_ranks + instance.sk_knowledge_dungeoneering_misc
	if instance.sk_knowledge_dungeoneering_class:
		instance.sk_knowledge_dungeoneering += 3
	instance.sk_knowledge_engineering = instance.ability_int_mod + instance.sk_knowledge_engineering_ranks + instance.sk_knowledge_engineering_misc
	if instance.sk_knowledge_engineering_class:
		instance.sk_knowledge_engineering += 3
	instance.sk_knowledge_geography = instance.ability_int_mod + instance.sk_knowledge_geography_ranks + instance.sk_knowledge_geography_misc
	if instance.sk_knowledge_geography_class:
		instance.sk_knowledge_geography += 3
	instance.sk_knowledge_history = instance.ability_int_mod + instance.sk_knowledge_history_ranks + instance.sk_knowledge_history_misc
	if instance.sk_knowledge_history_class:
		instance.sk_knowledge_history += 3
	instance.sk_knowledge_local = instance.ability_int_mod + instance.sk_knowledge_local_ranks + instance.sk_knowledge_local_misc
	if instance.sk_knowledge_local_class:
		instance.sk_knowledge_local += 3
	instance.sk_knowledge_nature = instance.ability_int_mod + instance.sk_knowledge_nature_ranks + instance.sk_knowledge_nature_misc
	if instance.sk_knowledge_nature_class:
		instance.sk_knowledge_nature += 3
	instance.sk_knowledge_nobility = skill(instance.sk_knowledge_nobility, instance.ability_int_mod, instance.sk_knowledge_nobility_ranks, instance.sk_knowledge_nobility_misc, instance.sk_knowledge_nobility_class)
	instance.sk_knowledge_planes = skill(instance.sk_knowledge_planes, instance.ability_int_mod, instance.sk_knowledge_planes_ranks, instance.sk_knowledge_planes_misc, instance.sk_knowledge_planes_class)
	instance.sk_knowledge_relgion = skill(instance.sk_knowledge_religion, instance.ability_int_mod, instance.sk_knowledge_religion_ranks, instance.sk_knowledge_religion_misc, instance.sk_knowledge_religion_class)
	instance.sk_linguistics = skill(instance.sk_linguistics, instance.ability_int_mod, instance.sk_linguistics_ranks, instance.sk_linguistics_misc, instance.sk_linguistics_class)
	instance.sk_perception = skill(instance.sk_perception, instance.ability_wis_mod, instance.sk_perception_ranks, instance.sk_perception_misc, instance.sk_perception_class)
	instance.sk_perform = skill(instance.sk_perform, instance.ability_cha_mod, instance.sk_perform_ranks, instance.sk_perform_misc, instance.sk_perform_class)
	instance.sk_profession = skill(instance.sk_profession, instance.ability_wis_mod, instance.sk_profession_ranks, instance.sk_profession_misc, instance.sk_profession_class)

def skill(skill, ability, skill_ranks, skill_misc, skill_class, armor_penalty=False):
	skill = ability + skill_ranks + skill_misc
	if not armor_penalty == False:
		skill -= armor_penalty
	if skill_class:
		skill += 3
	return skill
