# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from usuario.models import Eventos


class LoginForm(forms.Form):

#	class Meta:
#		model = User
#		fields = ('username', 'password',)

	username = forms.CharField(label='Nome de usuário', max_length=30)
	password = forms.CharField(label='Senha', max_length=30, widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not User.objects.filter(username=username):
			raise forms.ValidationError(u'Esse nome de usuário não existe')
		return username

	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if not authenticate(username=username, password=password):
			raise forms.ValidationError(u'Senha incorreta')
		return password

	def save(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		return authenticate(username=username, password=password)


class EventosForm(forms.ModelForm):
	class Meta:
		model = Eventos
		#exclude = ('user',)

	#data = forms.DateField(widget=CalendarWidget)