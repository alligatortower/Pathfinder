from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.user.username

class Character(models.Model):
	player = models.ForeignKey(UserProfile)
	avatar = models.ImageField(upload_to='character_avatars', blank=True)
	name = models.CharField(max_length=64)

	ability_str = models.IntegerField(default=0)
	ability_dex = models.IntegerField(default=0)
	ability_con = models.IntegerField(default=0)
	ability_wis = models.IntegerField(default=0)
	ability_int = models.IntegerField(default=0)
	ability_cha = models.IntegerField(default=0)

	level = models.IntegerField(default=1)
	hp = models.IntegerField(default=1)
	current_hp = models.IntegerField(default=1)

	base_class_1 = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=128,unique=True)
	gm = models.OneToOneField(User)
	characters = models.ManyToManyField(Character)
	#last_updated = models.DateTimeField(blank=True)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.user.username
