"""Funcoes comuns para serem usadas por outros arquivos"""

from random import randint

def iniciarAtributosAleatorios(lista, pontos):
        while pontos > 0:
				indiceAleatorio = randint(0, len(lista)-1)
				if ( lista[indiceAleatorio][0] < lista[indiceAleatorio][1]):
					lista[indiceAleatorio][0] += 1
					pontos -= 1
        print lista
