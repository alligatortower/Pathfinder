from main.forms import *
### VIEW LOGIC
def add_character_edit_data(character):	
	data = {}
	data['EditCharacter_Abilities_Form'] = EditCharacter_Abilities_Form(instance=character)
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




### CHARACTER LOGIC
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
	print instance.name
	instance.initiative_total = instance.ability_dex_mod + instance.initiative_misc
	instance.ac = instance.ability_dex_mod + instance.ac_armor + instance.ac_shield + instance.ac_natural + instance.ac_misc + instance.size_mod
	instance.cmb =  instance.ability_str_mod + instance.size_mod

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
	instance.base_attack_bonus_1 = base_attack_bonus_1_total
	instance.base_attack_bonus_2 = base_attack_bonus_2_total
	instance.base_attack_bonus_3 = base_attack_bonus_3_total
	instance.base_attack_bonus_4 = base_attack_bonus_4_total

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
