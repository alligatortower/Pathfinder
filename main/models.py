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
	size = models.CharField(default="-" , max_length = 20)
	gender = models.CharField(default="-" , max_length = 20)
	age = models.IntegerField(default=0 )
	height = models.IntegerField(default=0 )
	weight = models.IntegerField(default=0 )
	hair = models.CharField(default="-", max_length=20 )
	eyes = models.CharField(default="-", max_length=20)
	level = models.IntegerField(default=1)
	base_class_1 = models.CharField(max_length=20)

	#ability tab
	ability_str = models.IntegerField(default=0)
	ability_str_mod = models.IntegerField(default=0)
	ability_str_temp = models.IntegerField(default=0)

	ability_dex = models.IntegerField(default=0)
	ability_dex_mod = models.IntegerField(default=0)
	ability_dex_temp = models.IntegerField(default=0)

	ability_con = models.IntegerField(default=0)
	ability_con_mod = models.IntegerField(default=0)
	ability_con_temp = models.IntegerField(default=0)

	ability_wis = models.IntegerField(default=0)
	ability_wis_mod = models.IntegerField(default=0)
	ability_wis_temp = models.IntegerField(default=0)

	ability_int = models.IntegerField(default=0)
	ability_int_mod = models.IntegerField(default=0)
	ability_int_temp = models.IntegerField(default=0)

	ability_cha = models.IntegerField(default=0)
	ability_cha_mod = models.IntegerField(default=0)
	ability_cha_temp = models.IntegerField(default=0)

	speed_normal = models.IntegerField(default=0)
	speed_armor = models.IntegerField(default=0)
	speed_fly = models.IntegerField(default=0)
	speed_swim = models.IntegerField(default=0)
	speed_climb = models.IntegerField(default=0)

	#combat tab
	initiative = models.IntegerField(default=0)
	initiative_misc = models.IntegerField(default=0)

	bab = models.IntegerField(default=0)
	spell_resistance = models.IntegerField(default=0)

	ac = models.IntegerField(default=0)
	ac_natural = models.IntegerField(default=0)
	ac_misc = models.IntegerField(default=0)
	ac_armor = models.IntegerField(default=0)
	ac_shield = models.IntegerField(default=0)

	hp = models.IntegerField(default=1)
	current_hp = models.IntegerField(default=1)

	cmb = models.IntegerField(default=0)
	

	#skills tab
	sk_acrobatics =models.IntegerField(default=0)
	sk_acrobatics_ranks = models.IntegerField(default=0)
	sk_acrobatics_misc = models.IntegerField(default=0)
	sk_acrobatics_class = models.BooleanField(default=False) 

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
	
	sk_craft_type = models.CharField(default="-", max_length = 20) 
	sk_craft = models.IntegerField(default=0)
	sk_craft_ranks = models.IntegerField(default=0)
	sk_craft_misc = models.IntegerField(default=0)
	sk_craft_class = models.BooleanField(default=False) 

	sk_diplomacy = models.IntegerField(default=0)
	sk_diplomacy_ranks = models.IntegerField(default=0)
	sk_diplomacy_misc = models.IntegerField(default=0)
	sk_diplomacy_class = models.BooleanField(default=False) 
	
	sk_disable_devie =models.IntegerField(default=0)
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
	sk_perception_class = models.BooleanField(default=False) 

	sk_profession_type = models.CharField(default="-", max_length = 20)  
	sk_profession = models.IntegerField(default=0)
	sk_profession_ranks = models.IntegerField(default=0)
	sk_profession_misc = models.IntegerField(default=0)
	sk_profession_class = models.BooleanField(default=False) 

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
	sk_steahth_misc = models.IntegerField(default=0)
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
