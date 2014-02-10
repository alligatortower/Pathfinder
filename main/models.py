import pdb
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user.username


class Game(models.Model):
	name = models.CharField(max_length=128,unique=True)
	slug = models.SlugField(editable=False)
	gm = models.ForeignKey(User)
	last_updated = models.DateTimeField(auto_now=True,null=True)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Game, self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name

class Character(models.Model):
	#behind the scene
	created = models.DateTimeField(auto_now_add=True,null=True)	
	last_updated = models.DateTimeField(auto_now=True,null=True)
	slug = models.SlugField(editable=False)
	
	#displayed each page
	player = models.ForeignKey(User)
	name = models.CharField(max_length=64)
	current_game = models.ForeignKey(Game,blank=True,null=True)
	
	#default tab
	avatar = models.ImageField(upload_to='character_avatars', blank=True)
	alignment = models.CharField(default="-", max_length = 20)
	race = models.CharField(default="-", max_length = 20 )
	deity = models.CharField(default="-", max_length = 20 )
	size = models.CharField(default="Medium" , max_length = 20)
	size_mod = models.IntegerField(default=0)
	gender = models.CharField(default="-" , max_length = 20)
	age = models.IntegerField(default=0 )
	height = models.IntegerField(default=0 )
	weight = models.IntegerField(default=0 )
	hair = models.CharField(default="-", max_length=20 )
	eyes = models.CharField(default="-", max_length=20)
	discription = models.CharField(default="-", max_length=1000)

	#misc
	hd = models.CharField(max_length=10, default="1d6")
	total_levels = models.IntegerField(default=0)
	

	#ability tab
	ability_str_base = models.PositiveIntegerField(default=10)
	ability_str_score = models.PositiveIntegerField(default=0)
	ability_str_mod = models.IntegerField(default=0,db_column="ability_str_mod")
	ability_str_equip = models.IntegerField(default=0)
	ability_str_spell = models.IntegerField(default=0)
	ability_str_misc = models.IntegerField(default=0)
	ability_str_misc_total = models.IntegerField(default=0)

	ability_dex_base = models.PositiveIntegerField(default=10,db_column="ability_dex")
	ability_dex_score = models.PositiveIntegerField(default=0)
	ability_dex_mod = models.IntegerField(default=0,db_column="ability_dex_mod")
	ability_dex_equip = models.IntegerField(default=0)
	ability_dex_spell = models.IntegerField(default=0)
	ability_dex_misc = models.IntegerField(default=0)
	ability_dex_misc_total = models.IntegerField(default=0)
	
	ability_con_base = models.PositiveIntegerField(default=10)
	ability_con_score = models.PositiveIntegerField(default=0)
	ability_con_mod = models.IntegerField(default=0)
	ability_con_equip = models.IntegerField(default=0)
	ability_con_spell = models.IntegerField(default=0)
	ability_con_misc = models.IntegerField(default=0)
	ability_con_misc_total = models.IntegerField(default=0)

	ability_wis_base = models.PositiveIntegerField(default=10)
	ability_wis_score = models.PositiveIntegerField(default=0)
	ability_wis_mod = models.IntegerField(default=0)
	ability_wis_equip = models.IntegerField(default=0)
	ability_wis_spell = models.IntegerField(default=0)
	ability_wis_misc = models.IntegerField(default=0)
	ability_wis_misc_total = models.IntegerField(default=0)

	ability_int_base = models.PositiveIntegerField(default=10)
	ability_int_score = models.PositiveIntegerField(default=0)
	ability_int_mod = models.IntegerField(default=0)
	ability_int_equip = models.IntegerField(default=0)
	ability_int_spell = models.IntegerField(default=0)
	ability_int_misc = models.IntegerField(default=0)
	ability_int_misc_total = models.IntegerField(default=0)

	ability_cha_base = models.PositiveIntegerField(default=10)
	ability_cha_score = models.PositiveIntegerField(default=0)
	ability_cha_mod = models.IntegerField(default=0)
	ability_cha_equip = models.IntegerField(default=0)
	ability_cha_spell = models.IntegerField(default=0)
	ability_cha_misc = models.IntegerField(default=0)
	ability_cha_misc_total = models.IntegerField(default=0)


	#combat tab
	initiative_total = models.IntegerField(default=0)
	initiative_feat = models.IntegerField(default=0)
	initiative_misc = models.IntegerField(default=0)

	base_attack_bonus_1 = models.IntegerField(default=0)
	base_attack_bonus_2 = models.IntegerField(default=0)
	base_attack_bonus_3 = models.IntegerField(default=0)
	base_attack_bonus_4 = models.IntegerField(default=0)
	melee_attack_bonus_1 = models.IntegerField(default=0)
	melee_attack_bonus_2 = models.IntegerField(default=0)
	melee_attack_bonus_3 = models.IntegerField(default=0)
	melee_attack_bonus_4 = models.IntegerField(default=0)
	melee_attack_bonus_str_or_dex = models.CharField(max_length=3, default="str")
	ranged_attack_bonus_1 = models.IntegerField(default=0)
	ranged_attack_bonus_2 = models.IntegerField(default=0)
	ranged_attack_bonus_3 = models.IntegerField(default=0)
	ranged_attack_bonus_4 = models.IntegerField(default=0)
	base_attack_bonus_misc = models.IntegerField(default=0) 

	fortitude_save_total = models.IntegerField(default=0)
	fortitude_save_base = models.IntegerField(default=0)
	fortitude_save_temp = models.IntegerField(default=0)
	fortitude_save_racial = models.IntegerField(default=0)
	fortitude_save_equip = models.IntegerField(default=0)
	fortitude_save_feat = models.IntegerField(default=0)
	fortitude_save_misc = models.IntegerField(default=0)
	fortitude_save_misc_total = models.IntegerField(default=0)
	reflex_save_total = models.IntegerField(default=0)
	reflex_save_base = models.IntegerField(default=0)
	reflex_save_temp = models.IntegerField(default=0)
	reflex_save_racial = models.IntegerField(default=0)
	reflex_save_equip = models.IntegerField(default=0)
	reflex_save_feat = models.IntegerField(default=0)
	reflex_save_misc = models.IntegerField(default=0)
	reflex_save_misc_total = models.IntegerField(default=0)
	willpower_save_total = models.IntegerField(default=0)
	willpower_save_base = models.IntegerField(default=0)
	willpower_save_temp = models.IntegerField(default=0)
	willpower_save_racial = models.IntegerField(default=0)
	willpower_save_equip = models.IntegerField(default=0)
	willpower_save_feat = models.IntegerField(default=0)
	willpower_save_misc = models.IntegerField(default=0)
	willpower_save_misc_total = models.IntegerField(default=0)

	speed_base = models.IntegerField(default=0)
	speed_armor = models.IntegerField(default=0)
	speed_fly = models.IntegerField(default=0)
	speed_swim = models.IntegerField(default=0)
	speed_climb = models.IntegerField(default=0)

	spell_resistance = models.IntegerField(default=0)
	ac_total = models.IntegerField(default=0)
	ac_touch_total = models.IntegerField(default=0)
	ac_ff_total = models.IntegerField(default=0)
	ac_natural = models.IntegerField(default=0)
	ac_misc_total = models.IntegerField(default=0)
	ac_misc = models.IntegerField(default=0)
	ac_armor_total = models.IntegerField(default=0)
	ac_armor = models.IntegerField(default=0)
	ac_shield = models.IntegerField(default=0)
	ac_dodge = models.IntegerField(default=0)
	ac_deflection = models.IntegerField(default=0)
	
	armor_check_penalty = models.PositiveIntegerField(default=0)

	total_hp = models.IntegerField(default=1)
	current_hp = models.IntegerField(default=1)
	nonlethal_damage = models.IntegerField(default=0)

	combat_maneuver_bonus = models.IntegerField(default=0)
	combat_maneuver_bonus_misc = models.IntegerField(default=0)
	combat_maneuver_defense = models.IntegerField(default=0)
	combat_maneuver_defense_misc = models.IntegerField(default=0)

	#skills tab
	total_ranks = models.IntegerField(default=0)
	max_ranks = models.IntegerField(default=0)

	sk_acrobatics_ranks = models.IntegerField(default=0)
	sk_acrobatics_misc = models.IntegerField(default=0)
	sk_acrobatics_class = models.BooleanField(default=False) 
	sk_acrobatics =models.IntegerField(default=0,db_column="sk_acrobatics")

	sk_appraise =models.IntegerField(default=0)
	sk_appraise_ranks = models.IntegerField(default=0)
	sk_appraise_misc = models.IntegerField(default=0)
	sk_appraise_class = models.BooleanField(default=False) 

	sk_bluff = models.IntegerField(default=0)
	sk_bluff_ranks = models.IntegerField(default=0)
	sk_bluff_misc = models.IntegerField(default=0)
	sk_bluff_class = models.BooleanField(default=False) 
		
	sk_climb =models.IntegerField(default=0)
	sk_climb_ranks = models.IntegerField(default=0)
	sk_climb_misc = models.IntegerField(default=0)	
	sk_climb_class = models.BooleanField(default=False)	

	sk_diplomacy = models.IntegerField(default=0)
	sk_diplomacy_ranks = models.IntegerField(default=0)
	sk_diplomacy_misc = models.IntegerField(default=0)
	sk_diplomacy_class = models.BooleanField(default=False) 
	
	sk_disable_device =models.IntegerField(default=0)
	sk_disable_device_ranks = models.IntegerField(default=0)
	sk_disable_device_misc = models.IntegerField(default=0)
	sk_disable_device_class = models.BooleanField(default=False) 
	
	sk_disguise = models.IntegerField(default=0)
	sk_disguise_ranks = models.IntegerField(default=0)
	sk_disguise_misc = models.IntegerField(default=0)
	sk_disguise_class = models.BooleanField(default=False) 

	sk_escape_artist =models.IntegerField(default=0)
	sk_escape_artist_ranks = models.IntegerField(default=0)
	sk_escape_artist_misc = models.IntegerField(default=0)
	sk_escape_artist_class = models.BooleanField(default=False) 

	sk_fly = models.IntegerField(default=0)
	sk_fly_ranks = models.IntegerField(default=0)
	sk_fly_misc = models.IntegerField(default=0)
	sk_fly_class =models.BooleanField(default=False) 

	sk_handle_animal = models.IntegerField(default=0)
	sk_handle_animal_ranks = models.IntegerField(default=0)
	sk_handle_animal_misc = models.IntegerField(default=0)
	sk_handle_animal_class = models.BooleanField(default=False) 

	sk_heal = models.IntegerField(default=0)
	sk_heal_ranks = models.IntegerField(default=0)
	sk_heal_misc = models.IntegerField(default=0)
	sk_heal_class = models.BooleanField(default=False) 

	sk_intimidate = models.IntegerField(default=0)
	sk_intimidate_ranks = models.IntegerField(default=0)
	sk_intimidate_misc = models.IntegerField(default=0)
	sk_intimidate_class = models.BooleanField(default=False) 

	sk_knowledge_arcana = models.IntegerField(default=0)
	sk_knowledge_arcana_ranks = models.IntegerField(default=0)
	sk_knowledge_arcana_misc = models.IntegerField(default=0)
	sk_knowledge_arcana_class = models.BooleanField(default=False) 

	sk_knowledge_dungeoneering =models.IntegerField(default=0)
	sk_knowledge_dungeoneering_ranks = models.IntegerField(default=0)
	sk_knowledge_dungeoneering_misc = models.IntegerField(default=0)
	sk_knowledge_dungeoneering_class = models.BooleanField(default=False) 

	sk_knowledge_engineering = models.IntegerField(default=0)
	sk_knowledge_engineering_ranks = models.IntegerField(default=0)
	sk_knowledge_engineering_misc = models.IntegerField(default=0)
	sk_knowledge_engineering_class = models.BooleanField(default=False) 

	sk_knowledge_geography = models.IntegerField(default=0)
	sk_knowledge_geography_ranks = models.IntegerField(default=0)
	sk_knowledge_geography_misc = models.IntegerField(default=0)
	sk_knowledge_geography_class = models.BooleanField(default=False) 
	
	sk_knowledge_history = models.IntegerField(default=0)
	sk_knowledge_history_ranks = models.IntegerField(default=0)
	sk_knowledge_history_misc = models.IntegerField(default=0)
	sk_knowledge_history_class = models.BooleanField(default=False) 

	sk_knowledge_local = models.IntegerField(default=0)
	sk_knowledge_local_ranks = models.IntegerField(default=0)
	sk_knowledge_local_misc = models.IntegerField(default=0)
	sk_knowledge_local_class = models.BooleanField(default=False) 

	sk_knowledge_nature = models.IntegerField(default=0)
	sk_knowledge_nature_ranks = models.IntegerField(default=0)
	sk_knowledge_nature_misc = models.IntegerField(default=0)
	sk_knowledge_nature_class = models.BooleanField(default=False) 

	sk_knowledge_nobility = models.IntegerField(default=0)
	sk_knowledge_nobility_ranks = models.IntegerField(default=0)
	sk_knowledge_nobility_misc = models.IntegerField(default=0)
	sk_knowledge_nobility_class = models.BooleanField(default=False) 

	sk_knowledge_planes = models.IntegerField(default=0)
	sk_knowledge_planes_ranks = models.IntegerField(default=0)
	sk_knowledge_planes_misc = models.IntegerField(default=0)
	sk_knowledge_planes_class = models.BooleanField(default=False) 

	sk_knowledge_religion = models.IntegerField(default=0)
	sk_knowledge_religion_ranks = models.IntegerField(default=0)
	sk_knowledge_religion_misc = models.IntegerField(default=0)
	sk_knowledge_religion_class = models.BooleanField(default=False) 

	sk_linguistics = models.IntegerField(default=0)
	sk_linguistics_ranks = models.IntegerField(default=0)
	sk_linguistics_misc = models.IntegerField(default=0)
	sk_linguistics_class = models.BooleanField(default=False) 

	sk_perception = models.IntegerField(default=0)
	sk_perception_ranks = models.IntegerField(default=0)
	sk_perception_misc = models.IntegerField(default=0)
	sk_perception_class = models.BooleanField(default=False) 

	sk_perform = models.IntegerField(default=0)
	sk_perform_ranks = models.IntegerField(default=0)
	sk_perform_misc = models.IntegerField(default=0)
	sk_perform_class = models.BooleanField(default=False) 

	sk_ride = models.IntegerField(default=0)
	sk_ride_ranks = models.IntegerField(default=0)
	sk_ride_misc = models.IntegerField(default=0)
	sk_ride_class = models.BooleanField(default=False) 
	
	sk_sense_motive = models.IntegerField(default=0)
	sk_sense_motive_ranks = models.IntegerField(default=0)
	sk_sense_motive_misc = models.IntegerField(default=0)
	sk_sense_motive_class = models.BooleanField(default=False) 

	sk_sleight_of_hand = models.IntegerField(default=0)
	sk_sleight_of_hand_ranks = models.IntegerField(default=0)
	sk_sleight_of_hand_misc = models.IntegerField(default=0)
	sk_sleight_of_hand_class = models.BooleanField(default=False) 

	sk_spellcraft = models.IntegerField(default=0)
	sk_spellcraft_ranks = models.IntegerField(default=0)
	sk_spellcraft_misc = models.IntegerField(default=0)
	sk_spellcraft_class = models.BooleanField(default=False) 

	sk_stealth = models.IntegerField(default=0)
	sk_stealth_ranks = models.IntegerField(default=0)
	sk_stealth_misc = models.IntegerField(default=0)
	sk_stealth_class = models.BooleanField(default=False) 

	sk_survival = models.IntegerField(default=0)
	sk_survival_ranks = models.IntegerField(default=0)
	sk_survival_misc = models.IntegerField(default=0)
	sk_survival_class = models.BooleanField(default=False) 

	sk_swim = models.IntegerField(default=0)
	sk_swim_ranks = models.IntegerField(default=0)
	sk_swim_misc = models.IntegerField(default=0)
	sk_swim_class = models.BooleanField(default=False) 
	
	sk_use_magical_device = models.IntegerField(default=0)
	sk_use_magical_device_ranks = models.IntegerField(default=0)
	sk_use_magical_device_misc = models.IntegerField(default=0)
	sk_use_magical_device_class = models.BooleanField(default=False) 

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Character, self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name

class MultiSkill(models.Model):
	character = models.ForeignKey(Character)
	sk_craft_or_profession = models.CharField(max_length=10, default="craft")
	sk_domain = models.CharField(max_length=30)
	sk_total = models.IntegerField(default=0)
	sk_ranks = models.IntegerField(default=0)
	sk_misc = models.IntegerField(default=0)
	sk_class = models.BooleanField(default=False)
	
	class Meta:
		unique_together = (("character","sk_domain"),)

class BaseClass(models.Model):
	class_belongs_to = models.ForeignKey(Character, null=True, blank=True, default=None)
	class_name = models.CharField(max_length=30, default="Barbarian")
	class_levels = models.IntegerField(max_length=30, default=1)
	class_hit_die = models.CharField(max_length=10,default="1d6")
	class_is_favored = models.BooleanField(default=False)
	class_base_attack_bonus_1 = models.IntegerField(default=0)
	class_base_attack_bonus_2 = models.IntegerField(default=0)
	class_base_attack_bonus_3 = models.IntegerField(default=0)
	class_base_attack_bonus_4 = models.IntegerField(default=0)
	class_base_fortitude_save = models.IntegerField(default=0)
	class_base_reflex_save = models.IntegerField(default=0)
	class_base_willpower_save = models.IntegerField(default=0)

	class Meta:
		unique_together = (("class_belongs_to","class_name"),)

class Item(models.Model):
	owner = models.ForeignKey(Character, null=True, blank=True, default= None)
	current_game = models.ForeignKey(Game, null=True, blank=True, default= None)
	name = models.CharField(max_length=256, default="Equipment")
	cost = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)
	material = models.CharField(max_length=20, default="metal")
	description = models.CharField(max_length=500, default="---")

	def __unicode__(self):
		return self.name

class Equipment(Item):
	is_equipped = models.BooleanField(default=False)
	is_a = models.CharField(max_length=10, default="Weapon")
	size = models.CharField(max_length=10, default="medium")
	proficiency = models.CharField(max_length=10,default="Light")

class Armor(Equipment):
	ac_bonus = models.IntegerField(default=0)
	max_dex = models.IntegerField(null=True, blank=True, default=None)
	armor_check_penalty = models.IntegerField(default=0)
	spell_fail_chance = models.IntegerField(default=0)
	speed_if_base_20 = models.IntegerField(default=0)
	speed_if_base_30 = models.IntegerField(default=0)

class Weapon(Equipment):
	attack_bonus = models.IntegerField(default=0)
	damage = models.CharField(max_length=10, default="1d3")
	damage_type = models.CharField(max_length=10, default="S")
	weapon_type = models.CharField(max_length=20, default="simple")
	crit_muliplier = models.CharField(max_length=3, default="x2")
	crit_range = models.CharField(max_length=10, null=True)
	reach = models.IntegerField(blank=True, null=True)
	range_increment = models.IntegerField(blank=True, null=True)
	quantity = models.IntegerField(default=1)
