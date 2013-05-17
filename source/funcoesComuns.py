"""Funcoes comuns para serem usadas por outros arquivos"""

from random import randint
from math import fabs

VALOR = 0
MAX = 1
MIN = 2
NUM_IT = 100


def iniciarAtributosAleatoriosOld0(lista, pontos):
        flagRecursao = False
        while pontos > 0:
            indiceAleatorio = randint(0, len(lista)-1)
            if ( lista[indiceAleatorio][VALOR] < lista[indiceAleatorio][MAX]):
                lista[indiceAleatorio][VALOR] += 1
                pontos -= 1

        for indice in range(len(lista)):
            verificacaoIntervalo = lista[indice][VALOR] - lista[indice][MIN]
            print lista
            
            if verificacaoIntervalo < 0:
                flagRecursao = True
                listaTemporaria = lista[0:indice] + lista[indice+1:]
                for indiceIF in range(len(listaTemporaria)):
                    condicao = 1 if listaTemporaria[indiceIF][VALOR] > listaTemporaria[indiceIF][MIN] else 0
                    listaTemporaria[indiceIF][VALOR] -= condicao
                    pontos += condicao
                lista[indice][VALOR] += pontos if (-verificacaoIntervalo > pontos) else -verificacaoIntervalo
                pontos = 0 if (-verificacaoIntervalo > pontos) else (pontos + verificacaoIntervalo)
                
        if flagRecursao: iniciarAtributosAleatorios(lista,pontos)
        
        print lista


def iniciarAtributosAleatoriosOld1(lista, pontos):
    pontosAtuais = pontos
    for indice in range(len(lista)):
        lista[indice][VALOR] = randint(lista[indice][MIN], lista[indice][MAX])
        pontosAtuais -= lista[indice][VALOR]
    if fabs(pontosAtuais) > pontos/10:
        iniciarAtributosAleatorios(lista,pontos)
    print lista, pontosAtuais

def iniciarAtributosAleatorios(lista, pontos):
        listaAtual = [x[:] for x in lista]
        pontosAtuais = 2*pontos
        dist = abs(pontosAtuais - pontos)
	indice_NUM_IT = 0
        for i in range(NUM_IT):
                pontosAtuais = 0
                for indice in range(len(listaAtual)):
                        listaAtual[indice][VALOR] = randint(listaAtual[indice][MIN], listaAtual[indice][MAX])
                        pontosAtuais += listaAtual[indice][VALOR]
                dist_atual = abs(pontosAtuais - pontos)
                if dist_atual < dist:
                        for indice in range(len(lista)):
                                lista[indice][VALOR] = listaAtual[indice][VALOR]
                        dist = dist_atual
                        pontosFinais = pontosAtuais
			if dist == 0: return
        print lista, pontosFinais,indice_NUM_IT
    
    
