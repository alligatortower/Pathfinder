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
		fields = ('name', 'avatar', 'ability_str_base', "ability_dex_base", 'ability_con_base', 'ability_wis_base', 'ability_int_base','ability_cha_base','hp')

class EditCharacter_Details_Form(forms.ModelForm):
	size = forms.ChoiceField(choices=(("Small","Small"),("Medium","Medium"),("Large","Large"),))

	class Meta:
		model = Character
		fields = ("alignment","race","deity","size","gender","age","height","weight","hair","eyes")

	def save(self,commit=True, *args, **kwargs):
		instance = super(EditCharacter_Details_Form, self).save(commit=False)
		if commit:
			size_mod_update(instance)
			instance.save()
		return instance

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
		fields = ('current_hp','bab','ac_natural','ac_misc','initiative_misc','armor_check_penalty')

	def save(self,commit=True, *args, **kwargs):
		instance = super(EditCharacter_Combatstats_Form, self).save(commit=False)
		if commit:
			set_combatstats(instance)
			set_skills(instance)
			instance.save()
		return instance

class EditCharacter_Skills_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = (
			"sk_acrobatics_ranks","sk_acrobatics_misc", "sk_acrobatics_class",
			"sk_appraise_ranks","sk_appraise_misc","sk_appraise_class"
		)
	
	def save(self,commit=True, *args, **kwargs):
		instance = super(EditCharacter_Skills_Form, self).save(commit=False)
		if commit:
			craft_and_profession_skills = MultiSkill.objects.filter(character=instance)
			for value in craft_and_profession_skills:
				value.sk_total = skill(instance.ability_int_mod, value.sk_ranks, value.sk_misc, value.sk_class)
				value.save()

			set_skills(instance)
			instance.save()
		return instance

class AddCraftOrProfessionForm(forms.ModelForm):
	sk_craft_or_profession = forms.ChoiceField(choices=(("Craft","Craft"),("Profession","Profession"),))

	class Meta:
		model = MultiSkill 
		fields = ("sk_craft_or_profession","sk_domain","sk_ranks","sk_misc","sk_class")


class EditCraftOrProfessionForm(forms.ModelForm):

	class Meta:
		model = MultiSkill
		fields = ("sk_domain","sk_ranks","sk_misc","sk_class")

	def save(self,commit=True, *args, **kwargs):
		instance = super(EditCraftOrProfessionForm, self).save(commit=False)
		if commit:
			set_skills(instance.character)
			instance.character.save()
			instance.sk_total = skill(instance.character.ability_int_mod, instance.sk_ranks, instance.sk_misc, instance.sk_class)
			instance.save()
		return instance

class EditMaxRanksForm(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("max_ranks",)

class WhatToCreateForm(forms.Form):
	types_of_item = (
		("Weapon", "Weapon"),
		("Armor", "Armor"),
	)

	what = forms.ChoiceField(choices=types_of_item)

	class Meta:
		fields = ("what",)

class CreateItemForm(forms.ModelForm):

	class Meta:
		model = Item
		exclude = ("owner","current_game")

class CreateEquipmentForm(CreateItemForm):
	size = forms.ChoiceField(choices=(("Small","Small"),("Medium","Medium"),("Large","Large"),))

	class Meta(CreateItemForm.Meta):
		model = Equipment
		exclude = CreateItemForm.Meta.exclude + ("is_equipped",)

class CreateArmorForm(CreateEquipmentForm):
	proficiency = forms.ChoiceField(choices=(("Light","Light"),("Medium","Medium"),("Heavy","Heavy"),))
	is_a = forms.ChoiceField(choices=(("Armor","Armor"),("Shield","Shield"),))
	class Meta(CreateEquipmentForm.Meta):
		model = Armor

class CreateWeaponForm(CreateEquipmentForm):
	is_a = forms.ChoiceField(choices=(("Melee Weapon","Melee Weapon"),("Ranged Weapon","Ranged Weapon"),))
	damage_type = forms.ChoiceField(choices=(("slashing","slashing"),("piercing","piercing"),("bludgeoning","bludgeoning"),))
	proficiency = forms.ChoiceField(choices=(("simple","simple"),("martial","martial"),("exotic","exotic"),))
	weapon_type = forms.ChoiceField(choices=(("Light","Light"),("One-Handed","One-Handed"),("Two-Handed","Two-Handed"),))	

	class Meta(CreateEquipmentForm.Meta):
		model = Weapon
		exclude = CreateEquipmentForm.Meta.exclude + ("reach","ranged_increment","quantity")


def size_mod_update(instante):
	if instance.size == "Small":
		instance.size_mod = 1
	elif instance.size == "Medium":
		instance.size_mod = 0
	elif instance.size == "Large":
		instance.size_mod = -1
	
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
	instance.bab = instance.bab
	instance.initiative = instance.ability_dex_mod + instance.initiative_misc
	instance.ac = instance.ability_dex_mod + instance.ac_armor + instance.ac_shield + instance.ac_natural + instance.ac_misc + instance.size_mod
	instance.cmb = instance.bab + instance.ability_str_mod + instance.size_mod

def set_skills(instance):
	instance.total_ranks = instance.sk_acrobatics_ranks + instance.sk_appraise_ranks + instance.sk_bluff_ranks + instance.sk_climb_ranks + instance.sk_diplomacy_ranks + instance.sk_disable_device_ranks + instance.sk_disguise_ranks + instance.sk_escape_artist_ranks + instance.sk_fly_ranks + instance.sk_handle_animal_ranks + instance.sk_heal_ranks + instance.sk_intimidate_ranks + instance.sk_knowledge_arcana_ranks + instance.sk_knowledge_dungeoneering_ranks + instance.sk_knowledge_engineering_ranks + instance.sk_knowledge_geography_ranks + instance.sk_knowledge_history_ranks + instance.sk_knowledge_local_ranks + instance.sk_knowledge_nature_ranks + instance.sk_knowledge_nobility_ranks + instance.sk_knowledge_planes_ranks + instance.sk_knowledge_religion_ranks + instance.sk_linguistics_ranks + instance.sk_perception_ranks + instance.sk_perform_ranks + instance.sk_ride_ranks + instance.sk_sense_motive_ranks + instance.sk_sleight_of_hand_ranks + instance.sk_spellcraft_ranks + instance.sk_stealth_ranks + instance.sk_survival_ranks + instance.sk_swim_ranks + instance.sk_use_magical_device_ranks 
	multiskills = MultiSkill.objects.filter(character=instance)
	for value in multiskills:
		instance.total_ranks += value.sk_ranks

	instance.sk_acrobatics = skill(instance.ability_dex_mod, instance.sk_acrobatics_ranks, instance.sk_acrobatics_misc, instance.sk_acrobatics_class, instance.armor_check_penalty)
	instance.sk_appraise = skill(instance.ability_int_mod, instance.sk_appraise_ranks, instance.sk_appraise_misc, instance.sk_appraise_class)
	instance.sk_bluff = skill(instance.ability_cha_mod, instance.sk_bluff_ranks, instance.sk_bluff_misc, instance.sk_bluff_class)
	instance.sk_climb = skill(instance.ability_str_mod, instance.sk_climb_ranks, instance.sk_climb_misc, instance.sk_climb_class, instance.armor_check_penalty)
	instance.sk_diplomacy = skill(instance.ability_cha_mod, instance.sk_diplomacy_ranks, instance.sk_diplomacy_misc, instance.sk_diplomacy_class)
	instance.sk_disable_device = skill(instance.ability_dex_mod, instance.sk_disable_device_ranks, instance.sk_disable_device_misc, instance.sk_disable_device_class,  instance.armor_check_penalty)
	instance.sk_disguise = skill(instance.ability_cha_mod, instance.sk_disguise_ranks, instance.sk_disguise_misc, instance.sk_disguise_class)
	instance.sk_escape_artist = skill(instance.ability_dex_mod, instance.sk_escape_artist_ranks, instance.sk_escape_artist_misc, instance.sk_escape_artist_class, instance.armor_check_penalty)
	instance.sk_fly = skill(instance.ability_dex_mod, instance.sk_fly_ranks, instance.sk_fly_misc, instance.sk_fly_class, instance.armor_check_penalty)
	instance.sk_handle_animal = skill(instance.ability_cha_mod, instance.sk_handle_animal_ranks, instance.sk_handle_animal_misc, instance.sk_handle_animal_class)
	instance.sk_heal = skill(instance.ability_wis_mod, instance.sk_heal_ranks, instance.sk_heal_misc, instance.sk_heal_class)
	instance.sk_intimidate = skill(instance.ability_cha_mod, instance.sk_intimidate_ranks, instance.sk_intimidate_misc, instance.sk_intimidate_class)
	instance.sk_knowledge_arcana = skill(instance.ability_int_mod, instance.sk_knowledge_arcana_ranks, instance.sk_knowledge_arcana_misc, instance.sk_knowledge_arcana_class)
	instance.sk_knowledge_dungeoneering = skill(instance.ability_int_mod, instance.sk_knowledge_dungeoneering_ranks, instance.sk_knowledge_dungeoneering_misc, instance.sk_knowledge_dungeoneering_class)
	instance.sk_knowledge_engineering = skill(instance.ability_int_mod, instance.sk_knowledge_engineering_ranks, instance.sk_knowledge_engineering_misc, instance.sk_knowledge_engineering_class)
	instance.sk_knowledge_geography = skill(instance.ability_int_mod, instance.sk_knowledge_geography_ranks, instance.sk_knowledge_geography_misc, instance.sk_knowledge_geography_class)
	instance.sk_knowledge_history = skill(instance.ability_int_mod, instance.sk_knowledge_history_ranks, instance.sk_knowledge_history_misc, instance.sk_knowledge_history_class)
	instance.sk_knowledge_local = skill(instance.ability_int_mod, instance.sk_knowledge_local_ranks, instance.sk_knowledge_local_misc, instance.sk_knowledge_local_class)
	instance.sk_knowledge_nature = skill(instance.ability_int_mod, instance.sk_knowledge_nature_ranks, instance.sk_knowledge_nature_misc, instance.sk_knowledge_nature_class)
	instance.sk_knowledge_nobility = skill(instance.ability_int_mod, instance.sk_knowledge_nobility_ranks, instance.sk_knowledge_nobility_misc, instance.sk_knowledge_nobility_class)
	instance.sk_knowledge_planes = skill(instance.ability_int_mod, instance.sk_knowledge_planes_ranks, instance.sk_knowledge_planes_misc, instance.sk_knowledge_planes_class)
	instance.sk_knowledge_religion = skill(instance.ability_int_mod, instance.sk_knowledge_religion_ranks, instance.sk_knowledge_religion_misc, instance.sk_knowledge_religion_class)
	instance.sk_linguistics = skill(instance.ability_int_mod, instance.sk_linguistics_ranks, instance.sk_linguistics_misc, instance.sk_linguistics_class)
	instance.sk_perception = skill(instance.ability_wis_mod, instance.sk_perception_ranks, instance.sk_perception_misc, instance.sk_perception_class)
	instance.sk_perform = skill(instance.ability_cha_mod, instance.sk_perform_ranks, instance.sk_perform_misc, instance.sk_perform_class)
	instance.sk_ride = skill(instance.ability_dex_mod, instance.sk_ride_ranks, instance.sk_ride_misc, instance.sk_ride_class, instance.armor_check_penalty)
	instance.sk_sense_motive = skill(instance.ability_wis_mod, instance.sk_sense_motive_ranks, instance.sk_sense_motive_misc, instance.sk_sense_motive_class)
	instance.sk_sleight_of_hand = skill(instance.ability_dex_mod, instance.sk_sleight_of_hand_ranks, instance.sk_sleight_of_hand_misc, instance.sk_sleight_of_hand_class, instance.armor_check_penalty)
	instance.sk_spellcraft = skill(instance.ability_int_mod, instance.sk_spellcraft_ranks, instance.sk_spellcraft_misc, instance.sk_spellcraft_class)
	instance.sk_stealth = skill(instance.ability_dex_mod, instance.sk_stealth_ranks, instance.sk_stealth_misc, instance.sk_stealth_class, instance.armor_check_penalty)
	instance.sk_survival = skill(instance.ability_wis_mod, instance.sk_survival_ranks, instance.sk_survival_misc, instance.sk_survival_class)
	instance.sk_swim = skill(instance.ability_str_mod, instance.sk_swim_ranks, instance.sk_swim_misc, instance.sk_swim_class, instance.armor_check_penalty)
	instance.sk_use_magical_device = skill(instance.ability_cha_mod, instance.sk_use_magical_device_ranks, instance.sk_use_magical_device_misc, instance.sk_use_magical_device_class)

def skill(ability, skill_ranks, skill_misc, skill_class, armor_penalty=False):
	skill = ability + skill_ranks + skill_misc
	if not armor_penalty == False:
		skill -= armor_penalty
	if skill_class and skill_ranks > 0:
		skill += 3
	return skill
