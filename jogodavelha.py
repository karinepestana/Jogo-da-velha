import numpy as np
from random import randint
import time
import argparse
import copy


class Node:
	def __init__(self, data):        

		self.data = data
		self.h = 0

def expande():
	lista = []
	for i in range(0,size):
		for j in range(0,size):
			aux = copy.deepcopy(tabuleiro)
			if aux[i][j] == '0':
				aux[i][j] = 'x'
				lista.append(aux)
				aux = []
	return lista

def estado final(estado):
	if estado[0][0] == estado[0][1] == estado[0][2]:
		return True, estado[0][0]
	elif estado[1][0] == estado[1][1] == estado[1][2]:
		return True, estado[1][0]
	elif estado[2][0] == estado[2][1] == estado[2][2]:
		return True, estado[1][0]
	elif estado[0][0] == estado[1][0] == estado[2][0]:
		return True, estado[0][0]
	elif estado[0][1] == estado[1][1] == estado[2][1]:
		return True, estado[0][1]
	elif estado[0][2] == estado[1][2] == estado[2][2]:
		return True, estado[0][2]
	elif estado[0][0] == estado[1][1] == estado[2][2]:
		return True, estado[0][0]
	elif estado[0][2] == estado[1][1] == estado[2][0]:
		return True, estado[0][2]
	else return False, '0'

size = 3 
tabuleiro = np.array(['0', '0', '0', '0', '0', '0', '0', '0', '0']).reshape(size,size)

#while False:
print("Estado atual do tabuleiro:\n")
print(tabuleiro)
print("Entre com a posição que deseja jogar")
jogador2L = int(input("L:"))
jogador2C = int(input("C:"))

tabuleiro[jogador2L][jogador2C] = 'o'
saidas = expande()

print(saidas)
print("\n")
print(tabuleiro)





	


