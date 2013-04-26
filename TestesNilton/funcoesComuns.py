"""Funcoes comuns para serem usadas por outros arquivos"""

from random import randint

def iniciarAtributosAleatorios(lista, pontos):
        while pontos > 0:
                lista[randint(0, len(lista)-1)][0] += 1
                pontos -= 1
        print lista[0],lista[1],lista[2]
