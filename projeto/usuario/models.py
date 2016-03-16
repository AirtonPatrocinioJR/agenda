# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Eventos(models.Model):

	user = models.ForeignKey(User, verbose_name= 'usuario')
	titulo = models.CharField(u'Tirulo', max_length=30)
	data = models.DateField(u'Dia do evento')
	desc = models.TextField(u'Descrição', max_length=140)
	ativo = models.BooleanField(u'Evento Ativo', default= True, help_text=u'Marque para definir o contato como ativo')

	def __unicode__(self):
		return '%s %s %s' %(self.user.username, self.titulo, self.data)