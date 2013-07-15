"""Here we store functions that are going to be used by some objects"""

from random import randint
from math import fabs

VALUE = 0
MAX = 1
MIN = 2
NUM_IT = 100

'''
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
'''


def startRandomAttributes(attrList, points):
	'''This function distributes random values to the different attributes
	   of attrList of an object
	'''
        currentList = [x[:] for x in attrList]
        currentPoints = 2*points
        dist = abs(currentPoints - points)
	index_NUM_IT = 0
        for i in range(NUM_IT):
                currentPoints = 0
                for index in range(len(currentList)):
                        currentList[index][VALUE] = randint(currentList[index][MIN], currentList[index][MAX])
                        currentPoints += currentList[index][VALUE]
                current_dist = abs(currentPoints - points)
                if current_dist < dist:
                        for index in range(len(attrList)):
                                attrList[index][VALUE] = currentList[index][VALUE]
                        dist = current_dist
                        finalPoints = currentPoints
			if dist == 0: return
        #print attrList, finalPoints, index_NUM_IT
    
def vector3Sub(vector1, vector2):
	retVector = [0,0,0]
	retVector[0] = vector1[0] - vector2[0]
	retVector[1] = vector1[1] - vector2[1]
	retVector[2] = vector1[2] - vector2[2]
	return retVector
	
def vector2Module(vector1):
	retModule = 0
	retModule = (vector1[0]**2 + vector1[1]**2)**0.5
	return retModule
	
