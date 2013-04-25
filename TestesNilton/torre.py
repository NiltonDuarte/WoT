"""Tower Class File"""
from random import randint
from funcoesComuns import *

class Torre:
    """Classe que define os atributos e funcoes de uma torre"""

    
    def __init__(self):
        #Frequencia de diparo da Torre
        self.txDisparo = [None]
        self.txDisparoMin = 10
        self.txDisparoMax = 30
        #Alcance da visao da Torre
        self.alcanceVisao = [None]
        self.alcanceMin = 10
        self.alcanceMax = 20
        #Frequencia de criacao de Tropas
        self.txTropas = [None]
        self.txTropasMin = 10
        self.txTropasMax = 20
        
        self.listaAtributos = [self.txDisparo,self.txTropas,self.alcanceVisao]

	self.pontosIniciais = 100

	if (self.pontosIniciais <= (self.txDisparoMin+self.alcanceMin+self.txTropasMin) ):
	    self.txDisparo = self.txDisparoMin
	    self.alcanceVisao = self.alcanceMin
	    self.txTropas = self.txTropasMin
	    iniciarAtributosAletatorios(self.listaAtributos,self.pontosIniciais)
                     
                
torre = Torre()



