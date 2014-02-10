import pdb
import re
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
	size = forms.ChoiceField(choices=(("Small","Small"),("Medium","Medium"),("Large","Large"),))
	
	class Meta:
		model = Character
		fields = ('name', 'ability_str_base', "ability_dex_base", 'ability_con_base', 'ability_wis_base', 'ability_int_base','ability_cha_base','size','race','gender','age','alignment')

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
		fields = ('ability_str_base', 'ability_str_equip', 'ability_str_spell', 'ability_str_misc',
			'ability_dex_base',  'ability_dex_equip', 'ability_dex_spell', 'ability_dex_misc',
			'ability_con_base',  'ability_con_equip', 'ability_con_spell', 'ability_con_misc',
			'ability_wis_base',  'ability_wis_equip', 'ability_wis_spell', 'ability_wis_misc',
			'ability_int_base', 'ability_int_equip', 'ability_int_spell', 'ability_int_misc',
			'ability_cha_base', 'ability_cha_equip', 'ability_cha_spell', 'ability_cha_misc',)


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
		fields = ('current_hp','ac_natural','ac_misc','initiative_misc','armor_check_penalty')

	def __init__(self, *args, **kwargs):
		instance = super(EditCharacter_Combatstats_Form, self).__init__(*args, **kwargs)

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
			"sk_appraise_ranks","sk_appraise_misc","sk_appraise_class",
			"sk_bluff_ranks","sk_bluff_misc","sk_bluff_class",
			"sk_climb_ranks","sk_climb_misc","sk_climb_class",
			"sk_diplomacy_ranks","sk_diplomacy_misc","sk_diplomacy_class",
			"sk_disable_device_ranks","sk_disable_device_misc","sk_disable_device_class",
			"sk_disguise_ranks","sk_disguise_misc","sk_disguise_class",
			"sk_escape_artist_ranks","sk_escape_artist_misc","sk_escape_artist_class",
			"sk_fly_ranks","sk_fly_misc","sk_fly_class",
			"sk_handle_animal_ranks","sk_handle_animal_misc","sk_handle_animal_class",
			"sk_heal_ranks","sk_heal_misc","sk_heal_class",
			"sk_intimidate_ranks","sk_intimidate_misc","sk_intimidate_class",
			"sk_linguistics_ranks","sk_linguistics_misc","sk_linguistics_class",
			"sk_perception_ranks","sk_perception_misc","sk_perception_class",
			"sk_perform_ranks","sk_perform_misc","sk_perform_class",
			"sk_ride_ranks","sk_ride_misc","sk_ride_class",
			"sk_sense_motive_ranks","sk_sense_motive_misc","sk_sense_motive_class",
			"sk_sleight_of_hand_ranks","sk_sleight_of_hand_misc","sk_sleight_of_hand_class",
			"sk_spellcraft_ranks","sk_spellcraft_misc","sk_spellcraft_class",
			"sk_stealth_ranks","sk_stealth_misc","sk_stealth_class",
			"sk_survival_ranks","sk_survival_misc","sk_survival_class",
			"sk_swim_ranks","sk_swim_misc","sk_swim_class",
			"sk_use_magical_device_ranks","sk_use_magical_device_misc","sk_use_magical_device_class",
			"sk_knowledge_arcana_ranks","sk_knowledge_arcana_misc","sk_knowledge_arcana_class",
			"sk_knowledge_dungeoneering_ranks","sk_knowledge_dungeoneering_misc","sk_knowledge_dungeoneering_class",
			"sk_knowledge_engineering_ranks","sk_knowledge_engineering_misc","sk_knowledge_engineering_class",
			"sk_knowledge_geography_ranks","sk_knowledge_geography_misc","sk_knowledge_geography_class",
			"sk_knowledge_history_ranks","sk_knowledge_history_misc","sk_knowledge_history_class",
			"sk_knowledge_local_ranks","sk_knowledge_local_misc","sk_knowledge_local_class",
			"sk_knowledge_nature_ranks","sk_knowledge_nature_misc","sk_knowledge_nature_class",
			"sk_knowledge_nobility_ranks","sk_knowledge_nobility_misc","sk_knowledge_nobility_class",
			"sk_knowledge_planes_ranks","sk_knowledge_planes_misc","sk_knowledge_planes_class",
			"sk_knowledge_religion_ranks","sk_knowledge_religion_misc","sk_knowledge_religion_class",
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
class AddBaseClassForm(forms.ModelForm):
	base_attack_bonus = forms.CharField(max_length=20, initial="+0")

	class Meta:
		model = BaseClass
		fields = ("class_name", "class_levels", "class_is_favored","class_hit_die", "base_attack_bonus","class_base_fortitude_save","class_base_reflex_save", "class_base_willpower_save")
	
	def save(self,commit=True, *args, **kwargs):
		instance = super(AddBaseClassForm, self).save(commit=False)
		if commit:
			instance.save()
			character = Character.objects.get(name=instance.class_belongs_to)
			set_combatstats(character)
		return instance

class EditBaseClassForm(forms.ModelForm):
	base_attack_bonus = forms.CharField(max_length=20)

	class Meta:
		model = BaseClass
		fields = ("class_name", "class_levels", "class_is_favored", "class_hit_die","base_attack_bonus", "class_base_fortitude_save", "class_base_reflex_save", "class_base_willpower_save")

	def __init__(self, *args, **kwargs):
		instance = super(EditBaseClassForm, self).__init__(*args, **kwargs)
		bab_1 = kwargs['instance'].class_base_attack_bonus_1
		bab_2 = kwargs['instance'].class_base_attack_bonus_2
		bab_3 = kwargs['instance'].class_base_attack_bonus_3
		bab_4 = kwargs['instance'].class_base_attack_bonus_4
		initial_bab = "+" + str(bab_1) 
		initial_bab += "/+" + str(bab_2) if bab_2 > 0 else "" 
		initial_bab += "/+" + str(bab_3) if bab_3 > 0 else ""
		initial_bab += "/+" + str(bab_4) if bab_4 > 0 else ""
		self.fields['base_attack_bonus'].initial = initial_bab

	def save(self,commit=True, *args, **kwargs):
		instance = super(EditBaseClassForm, self).save(commit=False)
		if commit:
			bab_regex = re.findall(r'\+?(\d+)/?', self.cleaned_data['base_attack_bonus'])
			instance.class_base_attack_bonus_1 = int(bab_regex[0]) if 0 < len(bab_regex) else 0
			instance.class_base_attack_bonus_2 = int(bab_regex[1]) if 1 < len(bab_regex) else 0
			instance.class_base_attack_bonus_3 = int(bab_regex[2]) if 2 < len(bab_regex) else 0
			instance.class_base_attack_bonus_4 = int(bab_regex[3]) if 3 < len(bab_regex) else 0
			instance.save()
			character = Character.objects.get(name=instance.class_belongs_to)
			set_combatstats(character)
			print character.base_attack_bonus_3
			character.save()
		return instance



class EditBaseClassSavesForm(forms.ModelForm):

	class Meta:
		model = BaseClass
		fields = ("class_base_fortitude_save","class_base_reflex_save", "class_base_willpower_save")

class EditCharacter_Health_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("current_hp","total_hp","nonlethal_damage",)

class EditCharacter_Initiative_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("initiative_feat","initiative_misc",)

class EditCharacter_AC_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("ac_dodge","ac_deflection","ac_misc",)

class EditCharacter_Speed_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("speed_base","speed_armor","speed_fly","speed_climb","speed_swim")

class EditCharacter_BaseAttack_Form(forms.ModelForm):
	melee_attack_bonus_str_or_dex = forms.ChoiceField(choices=(("str","Strength"),("dex","Dexterity"),))

	class Meta:
		model = Character
		fields = ("melee_attack_bonus_str_or_dex", "base_attack_bonus_misc")

class EditCharacter_CombatManeuver_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("combat_maneuver_bonus_misc","combat_maneuver_defense_misc",)

class EditCharacter_Saves_Form(forms.ModelForm):

	class Meta:
		model = Character
		fields = ("fortitude_save_temp","fortitude_save_racial","fortitude_save_equip","fortitude_save_feat","fortitude_save_misc",
			"reflex_save_temp","reflex_save_racial","reflex_save_equip","reflex_save_feat","reflex_save_misc",
			"willpower_save_temp","willpower_save_racial","willpower_save_equip","willpower_save_feat","willpower_save_misc",)

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


def size_mod_update(instance):
	if instance.size == "Small":
		instance.size_mod = 1
	elif instance.size == "Medium":
		instance.size_mod = 0
	elif instance.size == "Large":
		instance.size_mod = -1
	
def set_abilities(instance):		
	instance.ability_str_misc_total = instance.ability_str_equip + instance.ability_str_spell + instance.ability_str_misc 
	instance.ability_str_score = instance.ability_str_base + instance.ability_str_misc_total
	instance.ability_str_mod = (instance.ability_str_score - 10) / 2
	
	instance.ability_dex_misc_total = instance.ability_dex_equip + instance.ability_dex_spell + instance.ability_dex_misc 
	instance.ability_dex_score = instance.ability_dex_base + instance.ability_dex_misc_total
	instance.ability_dex_mod = (instance.ability_dex_score - 10) / 2
	
	instance.ability_con_misc_total = instance.ability_con_equip + instance.ability_con_spell + instance.ability_con_misc 
	instance.ability_con_score = instance.ability_con_base + instance.ability_con_misc_total
	instance.ability_con_mod = (instance.ability_con_score - 10) / 2
	
	instance.ability_int_misc_total = instance.ability_int_equip + instance.ability_int_spell + instance.ability_int_misc 
	instance.ability_int_score = instance.ability_int_base + instance.ability_int_misc_total
	instance.ability_int_mod = (instance.ability_int_score - 10) / 2
	
	instance.ability_wis_misc_total = instance.ability_wis_equip + instance.ability_wis_spell + instance.ability_wis_misc 
	instance.ability_wis_score = instance.ability_wis_base + instance.ability_wis_misc_total
	instance.ability_wis_mod = (instance.ability_wis_score - 10) / 2

	instance.ability_cha_misc_total = instance.ability_cha_equip + instance.ability_cha_spell + instance.ability_cha_misc 
	instance.ability_cha_score = instance.ability_cha_base + instance.ability_cha_misc_total
	instance.ability_cha_mod = (instance.ability_cha_score - 10) / 2

def set_combatstats(instance):
	instance.initiative_total = instance.ability_dex_mod + instance.initiative_misc + instance.initiative_feat

	instance.ac_total = 10 + instance.ability_dex_mod + instance.ac_armor + instance.ac_shield + instance.ac_natural + instance.ac_misc + instance.size_mod + instance.ac_dodge + instance.ac_deflection
	instance.ac_touch_total = 10 + instance.ability_dex_mod + instance.size_mod + instance.ac_dodge + instance.ac_deflection
	instance.ac_ff_total = 10 + instance.ac_armor + instance.ac_shield + instance.ac_natural

	base_attack_bonus_1_total = 0
	base_attack_bonus_2_total = 0
	base_attack_bonus_3_total = 0
	base_attack_bonus_4_total = 0
	base_fortitude_save_total = 0
	base_reflex_save_total = 0
	base_willpower_save_total = 0
	base_classes = BaseClass.objects.filter(class_belongs_to=instance)
	if base_classes:
		for base_class in base_classes:
			base_attack_bonus_1_total += base_class.class_base_attack_bonus_1
			base_attack_bonus_2_total += base_class.class_base_attack_bonus_2
			base_attack_bonus_3_total += base_class.class_base_attack_bonus_3
			base_attack_bonus_4_total += base_class.class_base_attack_bonus_4

			base_fortitude_save_total += base_class.class_base_fortitude_save
			base_reflex_save_total += base_class.class_base_reflex_save
			base_willpower_save_total += base_class.class_base_willpower_save
	instance.base_attack_bonus_1 = base_attack_bonus_1_total + instance.base_attack_bonus_misc
	instance.base_attack_bonus_2 = base_attack_bonus_2_total
	instance.base_attack_bonus_3 = base_attack_bonus_3_total
	instance.base_attack_bonus_4 = base_attack_bonus_4_total
	if instance.base_attack_bonus_2 > 0:
		instance.base_attack_bonus_2 += instance.base_attack_bonus_misc
	if instance.base_attack_bonus_3 > 0:
		instance.base_attack_bonus_3 += instance.base_attack_bonus_misc
	if instance.base_attack_bonus_4 > 0:
		instance.base_attack_bonus_4 += instance.base_attack_bonus_misc

	instance.fortitude_save_base = base_fortitude_save_total
	instance.reflex_save_base = base_reflex_save_total
	instance.willpower_save_base = base_willpower_save_total
	if instance.melee_attack_bonus_str_or_dex == "str":
		instance.melee_attack_bonus_1 = instance.ability_str_mod + instance.base_attack_bonus_1
		instance.melee_attack_bonus_2 = instance.ability_str_mod + instance.base_attack_bonus_2
		instance.melee_attack_bonus_3 = instance.ability_str_mod + instance.base_attack_bonus_3
		instance.melee_attack_bonus_4 = instance.ability_str_mod + instance.base_attack_bonus_4
	if instance.melee_attack_bonus_str_or_dex == "dex":
		instance.melee_attack_bonus_1 = instance.ability_dex_mod + instance.base_attack_bonus_1
		instance.melee_attack_bonus_2 = instance.ability_dex_mod + instance.base_attack_bonus_2
		instance.melee_attack_bonus_3 = instance.ability_dex_mod + instance.base_attack_bonus_3
		instance.melee_attack_bonus_4 = instance.ability_dex_mod + instance.base_attack_bonus_4
	instance.ranged_attack_bonus_1 = instance.ability_dex_mod + instance.base_attack_bonus_1
	instance.ranged_attack_bonus_2 = instance.ability_dex_mod + instance.base_attack_bonus_2
	instance.ranged_attack_bonus_3 = instance.ability_dex_mod + instance.base_attack_bonus_3
	instance.ranged_attack_bonus_4 = instance.ability_dex_mod + instance.base_attack_bonus_4

	instance.combat_maneuver_bonus =  instance.ability_str_mod + instance.base_attack_bonus_1 + instance.combat_maneuver_bonus_misc
	instance.combat_maneuver_defense =  instance.ability_str_mod + instance.ability_dex_mod + instance.size_mod + instance.base_attack_bonus_1 + instance.combat_maneuver_defense_misc + 10

	instance.fortitude_save_total = instance.ability_con_mod + instance.fortitude_save_base + instance.fortitude_save_temp
	instance.reflex_save_total = instance.ability_dex_mod + instance.reflex_save_base + instance.reflex_save_temp
	instance.willpower_save_total = instance.ability_wis_mod + instance.willpower_save_base + instance.willpower_save_temp

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
