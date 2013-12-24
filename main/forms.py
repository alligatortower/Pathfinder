from django import forms
from main.models import UserProfile, Game
from django.contrib.auth.models import User

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
	name = forms.CharField(max_length=64)
	class Meta:
		model = Game
		fields = ('name',)
