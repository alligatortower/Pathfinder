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
	player = models.ForeignKey(User)
	avatar = models.ImageField(upload_to='character_avatars', blank=True)
	name = models.CharField(max_length=64)
	slug = models.SlugField(editable=False)
	current_game = models.ForeignKey(Game,blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True,null=True)	
	last_updated = models.DateTimeField(auto_now=True,null=True)

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
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Character, self).save(*args,**kwargs)

	def __unicode__(self):
		return self.name
