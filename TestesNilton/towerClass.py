"""Tower Class File"""
from random import randint

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
        
    def iniciarAtributosAletatorios(self,pontos):
        if (pontos <= (self.txDisparoMin+self.alcanceMin+self.txTropasMin) ):
            print "error"
        else:
            pontos -= (self.txDisparoMin+self.alcanceMin+self.txTropasMin)
            self.txDisparo[0] = self.txDisparoMin
            self.txTropas[0] = self.txTropasMin
            self.alcanceVisao[0] = self.alcanceMin
            while pontos > 0:
                self.listaAtributos[randint(0,2)][0] += 1
                pontos -= 1
        print self.listaAtributos[0],self.listaAtributos[1],self.listaAtributos[2]
                    
                
torre = Torre()
torre.iniciarAtributosAletatorios(100)


