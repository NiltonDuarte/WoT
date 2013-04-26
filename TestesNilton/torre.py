"""Tower Class File"""

from random import randint
from funcoesComuns import *
from projetil import *
from tropas import *

class Torre:
    """Classe que define os atributos e funcoes de uma torre"""

    
    def __init__(self):
		#Forca de disparo da Torre
        self.forcaDisparo = None
        self.forcaDisparoMin = 10
        self.forcaDisparoMax = 40
        self.listaForcaDisparo = [self.forcaDisparo, self.forcaDisparoMax]
        #Frequencia de diparo da Torre
        self.txDisparo = None #Nao usar esta variavel. Usar listaTxDisparo[0]
        self.txDisparoMin = 10
        self.txDisparoMax = 40
        self.listaTxDisparo = [self.txDisparo, self.txDisparoMax]
        #Alcance da visao da Torre
        self.alcanceVisao = None #Nao usar esta variavel! Usar listaAlcanceVisao[0]
        self.alcanceMin = 10
        self.alcanceMax = 40
        self.listaAlcanceVisao = [self.alcanceVisao, self.alcanceMax]
        #Frequencia de criacao de Tropas
        self.txTropas = None #Nao usar esta variavel! Usar listaTxTropas[0]
        self.txTropasMin = 10
        self.txTropasMax = 30
        self.listaTxTropas = [self.txTropas, self.txTropasMax]
		
        self.listaAtributos = [self.listaForcaDisparo, self.listaTxDisparo, self.listaAlcanceVisao, self.listaTxTropas]

        self.pontosIniciais = 100
        
        self.projetil = Projetil()
        
        
    
    def iniciarTorre(self):
		"""Inicia a torre com velores semi aleatorios"""
		if (self.pontosIniciais >= (self.forcaDisparoMin + self.txDisparoMin + self.alcanceMin + self.txTropasMin) and self.pontosIniciais <= (self.forcaDisparoMax + self.txDisparoMax + self.alcanceMax + self.txTropasMax)):            
            #Atribuindo valores minimos
			self.listaForcaDisparo[0] = self.forcaDisparoMin
			self.listaTxDisparo[0] = self.txDisparoMin
			self.listaAlcanceVisao[0] = self.alcanceMin
			self.listaTxTropas[0] = self.txTropasMin
            
            #Atribuindo valores maximos
			self.listaForcaDisparo[1] = self.forcaDisparoMax
			self.listaTxDisparo[1] = self.txDisparoMax
			self.listaAlcanceVisao[1] = self.alcanceMax
			self.listaTxTropas[1] = self.txTropasMax
			
            #Subtraindo valores ja atribuidos
			self.pontosIniciais -= (self.txDisparoMin + self.alcanceMin + self.txTropasMin)
            
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
                     
                




