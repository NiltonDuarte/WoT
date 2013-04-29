"""Funcoes comuns para serem usadas por outros arquivos"""

from random import randint
from math import fabs

VALUE = 0
MAX = 1
MIN = 2


def iniciarAtributosAleatoriosOld(lista, pontos):
        flagRecursao = False
        while pontos > 0:
            indiceAleatorio = randint(0, len(lista)-1)
            if ( lista[indiceAleatorio][VALUE] < lista[indiceAleatorio][MAX]):
                lista[indiceAleatorio][VALUE] += 1
                pontos -= 1

        for index in range(len(lista)):
            verificacaoIntervalo = lista[index][VALUE] - lista[index][MIN]
            print lista
            
            if verificacaoIntervalo < 0:
                flagRecursao = True
                listaTemporaria = lista[0:index] + lista[index+1:]
                for indexIF in range(len(listaTemporaria)):
                    condicao = 1 if listaTemporaria[indexIF][VALUE] > listaTemporaria[indexIF][MIN] else 0
                    listaTemporaria[indexIF][VALUE] -= condicao
                    pontos += condicao
                lista[index][VALUE] += pontos if (-verificacaoIntervalo > pontos) else -verificacaoIntervalo
                pontos = 0 if (-verificacaoIntervalo > pontos) else (pontos + verificacaoIntervalo)
                
        if flagRecursao: iniciarAtributosAleatorios(lista,pontos)
        
        print lista


def iniciarAtributosAleatorios(lista, pontos):
    pontosAtuais = pontos
    for index in range(len(lista)):
        lista[index][VALUE] = randint(lista[index][MIN], lista[index][MAX])
        pontosAtuais -= lista[index][VALUE]
    if fabs(pontosAtuais) > pontos/10:
        iniciarAtributosAleatorios(lista,pontos)
    print lista, pontosAtuais
    
    