from bd import *
from usuario import *
from config import *

def acesso(usuario):
	sair = False
	while not sair:
		if usuario["tipo"] == "aluno":
			print("\nBem vindo aluno "+usuario["nome"])
			print("1) Cadastrar idiomas\n")
			print("2) Cadastrar horario e dia\n")
			print("3) Cadastrar cidade e estado\n")
			print("4) Mostrar seus dados\n")
			print("5) Encerrar sessão\n")
			escolha = int(input())
			if escolha == 1:
				cadastrarIdiomas(usuario)
			elif escolha == 2:
				cadastrarHorarios(usuario)
				cadastrarDias(usuario)
			elif escolha == 3:
				cadastrarCidade(usuario)
			elif escolha == 4:
				mostrarUsuario(usuario)
			elif escolha == 5:
				sair = True
			else:
				print("Opcao invalida\n")
		else:
			print("\nBem-vindo professor "+usuario["nome"])
			print("1) Cadastrar notas\n")
			print("2) Cadastrar faltas\n")
			print("3) Cadastrar disciplina\n")
			print("4) Mostrar seus dados\n")
			print("5) Encerrar sessão\n")
			escolha = int(input())
			if escolha == 1:
				cadastrarNotas()
			elif escolha == 2:
				cadastrarFaltas()
			elif escolha == 3:
				cadastrarDisciplinas(usuario)
			elif escolha == 4:
				mostrarUsuario(usuario)
			elif escolha == 5:
				sair = True
			else:
				print("Opcao invalida\n")

def main():
	sair = False
	while not sair:
		print("\nBem vindo ao Sistema de Idiomas!\n")
		print("1) Para realizar um novo cadastro\n")
		print("2) Para fazer login no sistema\n")
		print("3) Para sair\n")
		escolha = int(input())
		if escolha == 1:
			cadastrarUsuario()
		elif escolha == 2:
			nomeUsuario = input("Digite o nome de usuario\n")
			senha = input("Digite sua senha\n")
			if login(nomeUsuario, senha):
				usuarioAtual = buscarUsuario(nomeUsuario)
				acesso(usuarioAtual)
		elif escolha == 3:
			sair = True
		else:
			print("Opcao invalida\n")

main()


modeloAluno = {"nome":"",
			   "email":"",
			   "login":"",
			   "senha":"",
			   "tipo":"aluno",
			   "idiomas":"",
			   "horarios":"",
			   "dias":"",
			   "cidade":"",
			   "notas":"",
			   "faltas":""
		  	  }

modeloProfessor = {"nome":"",
				   "email":"",
				   "login":"",
				   "senha":"",
				   "tipo":"professor",
				   "disciplinas":""
				   }

idiomasDisponiveis = {1:"Português", 2:"Inglês", 3:"Francês",
					  4:"Alemão", 5:"Espanhol"}

horariosDisponiveis = {1:"07:00 - 8:40", 2:"08:50 - 10:30", 3:"10:50 - 12:30",
					   4:"13:00 - 14:30", 5:"15:00 - 17:00"}

diasDisponiveis = {1:"Segunda-feira", 2:"Terca-feira", 3:"Quarta-feira",
				   4:"Quinta-feira", 5:"Sexta-feira", 6:"Sabado"}


cidadesDisponiveis = {1:"Mossoró-RN", 2:"Natal-RN", 3:"Apodi-RN", 4:"Fortaleza-CE",
					  5:"Joao Pessoa-PB", 6:"Campina Grande-PB"}

caminho = "logins/"

import os
from config import *

def salvarUsuario(usuario):
	arq = open(caminho+usuario["login"], "w")
	for key in usuario.keys():
		arq.write(usuario[key])
		arq.write("\n")


def buscarUsuario(login):
	arq = open(caminho+login, "r")
	dados = arq.read()
	listaDados = dados.split("\n")
	if "aluno" in dados:
		usuario = modeloAluno
	else:
		usuario = modeloProfessor
	cont = 0
	for key in usuario.keys():
		usuario[key] = listaDados[cont]
		cont+=1
	return usuario

def usuarioExiste(nomeUsuario):
	try:
		arquivo = open(caminho+nomeUsuario, "r")
		return True
	except FileNotFoundError:
		return False

def pegarSenha(nomeUsuario):
	arquivo = open(caminho+nomeUsuario, "r")
	dados = buscarUsuario(nomeUsuario)
	return dados["senha"]

def cadastrarUsuario():
	if not os.path.exists(caminho):
		os.makedirs(caminho)
	usuario = criarUsuario()
	if usuarioExiste(usuario["login"]):
		print("Login ja cadastrado\n")
		return False

	if usuario["tipo"] == "aluno":
		novoUsuario = modeloAluno
	else:
		novoUsuario = modeloProfessor

	for key in novoUsuario.keys():
		if key in usuario:
			novoUsuario[key] = usuario[key]
	salvarUsuario(novoUsuario)
	return novoUsuario

def login(nomeUsuario, senha):
	if usuarioExiste(nomeUsuario) == False:
		print("Usuário não cadastrado")
		return False

	senhaCorreta = pegarSenha(nomeUsuario)
	if senha != senhaCorreta:
		print("Senha incorreta")
		return False

	return True

def criarUsuario():
	usuario = {}
	usuario["nome"] = input("Digite seu nome\n")
	usuario["email"] = input("Digite seu email\n")
	usuario["login"] = input("Digite seu login\n")
	usuario["senha"] = input("Digite sua senha\n")
	opcoes = ["aluno", "professor"]
	tipo = input("Vc é um professor ou um aluno?\n")
	while tipo not in opcoes:
		tipo = input("Vc é um professor ou um aluno?\n")
	usuario["tipo"] = tipo
	return usuario

def listarAlunos():
	arquivos = os.listdir(caminho)
	alunos = []
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["tipo"] == "aluno":
			alunos.append(atual["nome"])

	return alunos

def listarProfessores():
	arquivos = os.listdir(caminho)
	professores = []
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["tipo"] == "professor":
			professores.append(atual["nome"])

	return professores

def buscarPorNome(nome):
	arquivos = os.listdir(caminho)
	for i in range(len(arquivos)):
		atual = buscarUsuario(arquivos[i])
		if atual["nome"] == nome:
			return atual


from bd import *
from config import *


def cadastrarIdiomas(usuario):
	for c, v in idiomasDisponiveis.items():
		print("Digite " + str(c) + " para escolher " + v)
	escolha = int(input())
	if escolha in idiomasDisponiveis.keys():
		if usuario["idiomas"] == "":
			usuario["idiomas"] = idiomasDisponiveis[escolha]
		elif idiomasDisponiveis[escolha] in usuario["idiomas"]:
			print("Idioma ja cadastrado\n")
			return None
		else:
			idiomasAtuais = usuario["idiomas"] + ", " + idiomasDisponiveis[escolha]
			usuario["idiomas"] = idiomasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Idioma cadastrado com sucesso\n")


def cadastrarHorarios(usuario):
	for c, v in horariosDisponiveis.items():
		print("Digite " + str(c) + " para escolher " + v)
	escolha = int(input())
	if escolha in horariosDisponiveis.keys():
		if usuario["horarios"] == "":
			usuario["horarios"] = horariosDisponiveis[escolha]
		elif horariosDisponiveis[escolha] in usuario["horarios"]:
			print("Horario ja cadastrado\n")
			return None
		else:
			horariosAtuais = usuario["horarios"] + ", " + horariosDisponiveis[escolha]
			usuario["horarios"] = horariosAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Horario cadastrado com sucesso\n")


def cadastrarDias(usuario):
	for c, v in diasDisponiveis.items():
		print("Digite " + str(c) + " para escolher " + v)
	escolha = int(input())
	if escolha in diasDisponiveis.keys():
		if usuario["dias"] == "":
			usuario["dias"] = diasDisponiveis[escolha]
		elif diasDisponiveis[escolha] in usuario["dias"]:
			print("Dia ja cadastrado\n")
			return None
		else:
			diasAtuais = usuario["dias"] + ", " + diasDisponiveis[escolha]
			usuario["dias"] = diasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Dia cadastrado com sucesso\n")


def cadastrarCidade(usuario):
	for c, v in cidadesDisponiveis.items():
		print("Digite " + str(c) + " para escolher " + v)
	escolha = int(input())
	if escolha in cidadesDisponiveis.keys():
		usuario["cidade"] = cidadesDisponiveis[escolha]

	salvarUsuario(usuario)
	print("Cidade cadastrada com sucesso\n")


def cadastrarNotas():
	print("Escolha o aluno que deseja cadastrar a nota. Alunos disponíveis:\n")
	print(listarAlunos())
	escolhido = input()
	nota = input("Digite a nota\n")
	usuario = buscarPorNome(escolhido)
	if usuario != None:
		if usuario["notas"] == "":
			usuario["notas"] = nota
		else:
			notasAtuais = usuario["notas"] + ", " + nota
			usuario["notas"] = notasAtuais
	else:
		print("Usuario nao encontrado! Favor, considerar letras maiusculas e minusculas\n")
		return None

	salvarUsuario(usuario)
	print("Nota cadastrada com sucesso\n")


def cadastrarFaltas():
	print("Escolha o aluno que deseja cadastrar a falta. Alunos disponíveis:\n")
	print(listarAlunos())
	escolhido = input()
	usuario = buscarPorNome(escolhido)
	if usuario != None:
		quantidade = int(input("Digite a quantidade de faltas\n"))
		if usuario["faltas"] == "":
			usuario["faltas"] = str(quantidade)
		else:
			faltasAtuais = int(usuario["faltas"]) + quantidade
			usuario["faltas"] = str(faltasAtuais)
	else:
		print("Usuario nao encontrado! Favor, considerar letras maiusculas e minusculas\n")
		return None

	salvarUsuario(usuario)
	print("Falta(s) cadastrada com sucesso\n")


def cadastrarDisciplinas(usuario):
	for c, v in idiomasDisponiveis.items():
		print("Digite " + str(c) + " para escolher " + v)
	escolha = int(input())
	if escolha in idiomasDisponiveis.keys():
		if usuario["disciplinas"] == "":
			usuario["disciplinas"] = idiomasDisponiveis[escolha]
		elif idiomasDisponiveis[escolha] in usuario["disciplinas"]:
			print("Disciplina ja cadastrada\n")
			return None
		else:
			disciplinasAtuais = usuario["disciplinas"] + ", " + idiomasDisponiveis[escolha]
			usuario["disciplinas"] = disciplinasAtuais
	else:
		print("Opcao invalida\n")
		return None

	salvarUsuario(usuario)
	print("Disciplina cadastrada com sucesso\n")


def mostrarUsuario(usuario):
	for key in usuario.keys():
		if usuario[key] != "":
			print(str(key) + ": " + usuario[key])


