# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios
from usuario.forms import LoginForm, EventosForm
from usuario.models import Eventos

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User


def index(request):
	next = request.REQUEST.get('next', '//')
	eventos = Eventos.objects.all()
	usuarios = User.objects.all()
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		form2 = EventosForm(request.POST)
		#form2.usuario.id = User.objects.get(user_id)
		if form.is_valid():
			# processa o formulario
			user = form.save()
			login(request, user)
			#usuarios = User.objects.all()
			return HttpResponseRedirect(next)
		
		if form2.is_valid():
			# processa o formulario
			novo_evento = form2.save()
			#login(request, user)
			return HttpResponseRedirect(next)

	else:
		form = LoginForm()
		form2 = EventosForm()

	return render(request, "usuario/index.html", {"form": form, "form2": form2, "next": next, "eventos": eventos, "usuarios": usuarios,})



def sair(request):
	logout(request)
	return HttpResponseRedirect(reverse('usuario_index'))

# pagina inicial do projeto django-wars
def index2(request):
	usuarios = User.objects.all()
	return render_to_response("usuario/index.html", {"usuarios":usuarios,})

# pagina de cadastro 
def registrar(request):

	# Se dados forem passados via POST
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid(): # se o formulario for valido
			form.save() # cria um novo usuario a partir dos dados enviados 
			return HttpResponseRedirect(reverse('usuario_index')) # redireciona para a tela de login
		else:
			# mostra novamente o formulario de cadastro com os erros do formulario atual
			return render(request, "usuario/registrar.html", {"form": form})

	# se nenhuma informacao for passada, exibe a pagina de cadastro com o formulario
	return render(request, "usuario/registrar.html", {"form": UserCreationForm() })