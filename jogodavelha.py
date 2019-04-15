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
			if aux[i][j] == 0:
				aux[i][j] = "x"
				lista.append(aux)
				aux = []
	return lista

tabuleiro = []
size = 3 
for i in range(size):
	tabuleiro.append([0]*size)

#while False:
print("Estado atual do tabuleiro:\n")
print(tabuleiro)
print("Entre com a posição que deseja jogar")
jogador2L = int(input("L:"))
jogador2C = int(input("C:"))

tabuleiro[jogador2L][jogador2C] = "o"
saidas = expande()

print(saidas)
print("\n")
print(tabuleiro)





	


