"""Tower Class File"""

from random import randint
from funcoesComuns import *
from projetil import *
from tropas import *

class Torre:
    """Classe que define os atributos e funcoes de uma torre"""

    
    def __init__(self, iniciarTorreFunc = False, pontos=0, lista=[]):
	#Forca de disparo da Torre
        self.forcaDisparo = 0
        self.forcaDisparoMin = 10
        self.forcaDisparoMax = 40
        self.listaForcaDisparo = [self.forcaDisparo, self.forcaDisparoMax, self.forcaDisparoMin]

        #Frequencia de diparo da Torre
        self.txDisparo = 0 #Nao usar esta variavel. Usar listaTxDisparo[0]
        self.txDisparoMin = 10
        self.txDisparoMax = 40
        self.listaTxDisparo = [self.txDisparo, self.txDisparoMax, self.txDisparoMin]

        #Alcance da visao da Torre
        self.alcanceVisao = 0 #Nao usar esta variavel! Usar listaAlcanceVisao[0]
        self.alcanceVisaoMin = 10
        self.alcanceVisaoMax = 40
        self.listaAlcanceVisao = [self.alcanceVisao, self.alcanceVisaoMax, self.alcanceVisaoMin]

        #Frequencia de criacao de Tropas
        self.txTropas = 0 #Nao usar esta variavel! Usar listaTxTropas[0]
        self.txTropasMin = 10
        self.txTropasMax = 30
        self.listaTxTropas = [self.txTropas, self.txTropasMax, self.txTropasMin]

        self.listaAtributos = [self.listaForcaDisparo, self.listaTxDisparo, self.listaAlcanceVisao, self.listaTxTropas]

        self.pontosIniciais = 300
        
        self.projetil = Projetil()
        self.tropa = Tropa()
        
        if (len(lista) > 0 and pontos and iniciarTorreFunc):
            self.pontosIniciais = pontos
            self.definirParametros(lista)
            self.iniciarTorre()
            
    def iniciarTorre(self):
		"""Inicia a torre com velores semi aleatorios"""
		if (self.pontosIniciais >= \
            (self.forcaDisparoMin + self.txDisparoMin + self.alcanceVisaoMin + self.txTropasMin) \
            and self.pontosIniciais <= \
            (self.forcaDisparoMax + self.txDisparoMax + self.alcanceVisaoMax + self.txTropasMax)):            
            #Atribuindo valores minimos
			self.listaForcaDisparo[MIN] = self.forcaDisparoMin
			self.listaTxDisparo[MIN] = self.txDisparoMin
			self.listaAlcanceVisao[MIN] = self.alcanceVisaoMin
			self.listaTxTropas[MIN] = self.txTropasMin
            
            #Atribuindo valores maximos
			self.listaForcaDisparo[MAX] = self.forcaDisparoMax
			self.listaTxDisparo[MAX] = self.txDisparoMax
			self.listaAlcanceVisao[MAX] = self.alcanceVisaoMax
			self.listaTxTropas[MAX] = self.txTropasMax
            
            #Atribuindo pontos aleatorios
			iniciarAtributosAleatorios(self.listaAtributos, self.pontosIniciais)
		else:
			print "Erro com quantidade de pontos iniciais da torre"
			
			
    def definirParametros(self,lista):
		"""Atribui os valores da lista nos recpectivos parametros
			[@forcaDisparoMin, @forcaDisparoMax, 
			 @txDisparoMin, @txDisparoMax,
			 @alcanceVisaoMin, @alcanceVisaoMax,
			 @txTropasMin, @txTropasMax]
		"""
		if len(lista) != 8: print "Erro com tamanho da lista de parametros da torre"; return
		self.forcaDisparoMin = lista[0]
		self.forcaDisparoMax = lista[1]
		self.txDisparoMin = lista[2]
		self.txDisparoMax = lista[3]
		self.alcanceVisaoMin = lista[4]
		self.alcanceVisaoMax = lista[5]
		self.txTropasMin = lista[6]
		self.txTropasMax = lista[7]


    def setPontosIniciais(self, pontos):
        self.pontosIniciais = pontos
                




