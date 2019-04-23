import numpy as np
from random import randint
import time
import argparse
import copy


class Node:
	def __init__(self, data):        

		self.data = data
		self.h = 0
		self.nodo_pai = None
		self.filhos = None

	def insert(self, lista):
		nos = self.filhos
		estado = None
		while nos:
			estado = nos.pop(0)

			if estado.filhos != None:
				nos.extend(estado.filhos)
			else:
				break
		if estado == None:
			self.filhos = lista
		else:
			estado.filhos = lista	

def expande(tabuleiro):
	lista = []
	for i in range(0,size):
		for j in range(0,size):
			aux = copy.deepcopy(tabuleiro.data)
			if aux[i][j] == '0':
				aux[i][j] = 'x'
				nodo = Node(aux)
				nodo.nodo_pai = tabuleiro
				lista.append(nodo)
				aux = []
	return lista

def min_max(lista_dados, nodo):
	estado_atual = None
	while lista_dados:
		estado_atual = lista_dados.pop(0)
		#nos_abertos = nos_abertos +1

		lista = expande(estado_atual)
		nodo.insert(lista)
		if lista:
			lista_dados.extend(lista)
		

def estado_final(estado):
	if estado[0][0] == estado[0][1] == estado[0][2] == 'x':
		return True, estado[0][0]
	elif estado[1][0] == estado[1][1] == estado[1][2] == 'x':
		return True, estado[1][0]
	elif estado[2][0] == estado[2][1] == estado[2][2] == 'x':
		return True, estado[1][0]
	elif estado[0][0] == estado[1][0] == estado[2][0] == 'x':
		return True, estado[0][0]
	elif estado[0][1] == estado[1][1] == estado[2][1] == 'x':
		return True, estado[0][1]
	elif estado[0][2] == estado[1][2] == estado[2][2] == 'x':
		return True, estado[0][2]
	elif estado[0][0] == estado[1][1] == estado[2][2] == 'x':
		return True, estado[0][0]
	elif estado[0][2] == estado[1][1] == estado[2][0] == 'x':
		return True, estado[0][2]
	else:
		return False, '0'

size = 3 
tabuleiro = np.array(['0', '0', '0', '0', '0', '0', '0', '0', '0']).reshape(size,size)
nivel = 0
nodo = Node(tabuleiro)

#while estado_final(nodo.data) == list(False, '0'):
print("Estado atual do tabuleiro:\n")
print(nodo.data)
print("Entre com a posição que deseja jogar")
jogador2L = int(input("L:"))
jogador2C = int(input("C:"))
nivel = nivel + 1

nodo.data[jogador2L][jogador2C] = 'o'

lista_dados = list()
lista_dados.append(nodo)
min_max(lista_dados, nodo)
print("FIM")









	


